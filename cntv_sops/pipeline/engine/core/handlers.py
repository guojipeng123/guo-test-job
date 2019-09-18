# -*- coding: utf-8 -*-

from __future__ import absolute_import
import logging
import traceback
from collections import namedtuple

from pipeline.exceptions import PipelineException
from pipeline.core.flow import activity, gateway, event
from pipeline.core.data.hydration import (
    hydrate_node_data,
    hydrate_data
)
from pipeline.engine import states, signals, exceptions
from pipeline.engine.models import (
    Status,
    Data,
    PipelineProcess,
    ScheduleService,
    LoopActivityHistory,
    LoopActivityStatus
)
from django_signal_valve import valve

logger = logging.getLogger('celery')
HandleResult = namedtuple('HandleResult', 'next_node should_return should_sleep')


# handlers

def loop_service_activity_handler(process, loop_service_act):
    success = False
    error_occurred = False
    ex_data = None

    # prepare data
    is_retrying = getattr(loop_service_act, 'retrying', False)
    setattr(loop_service_act, 'retrying', None)
    if not is_retrying:
        loop_service_act.prepare_loop_data()

    # hydrate inputs
    hydrate_node_data(loop_service_act)

    try:
        success = loop_service_act.execute(process.root_pipeline.data)
    except Exception as e:
        if loop_service_act.error_ignorable:
            success = True
            error_occurred = True
            loop_service_act.ignore_error()
        else:
            # send activity error signal
            valve.send(signals, 'activity_failed', sender=process.root_pipeline,
                       pipeline_id=process.root_pipeline.id,
                       pipeline_activity_id=loop_service_act.id)
        ex_data = traceback.format_exc(e)
        loop_service_act.data.set_outputs('ex_data', ex_data)
        logger.error(ex_data)

    if not success:
        ex_data = loop_service_act.data.get_one_of_outputs('ex_data')
        Status.objects.fail(loop_service_act, ex_data)
        LoopActivityHistory.objects.record(loop_service_act)
        LoopActivityStatus.objects.refresh_status(loop_service_act)

        try:
            loop_service_act.failure_handler(process.root_pipeline.data)
        except Exception as e:
            logger.error('failure_handler(%s) failed: %s' % (loop_service_act.id, traceback.format_exc(e)))

        # send activity error signal
        valve.send(signals, 'activity_failed', sender=process.root_pipeline,
                   pipeline_id=process.root_pipeline.id,
                   pipeline_activity_id=loop_service_act.id)

        return HandleResult(next_node=None, should_return=False, should_sleep=True)

    else:
        if loop_service_act.need_schedule() and not error_occurred:
            version = Status.objects.get(id=loop_service_act.id).version
            ScheduleService.objects.set_schedule(loop_service_act.id, service_act=loop_service_act.shell(),
                                                 process_id=process.id, version=version,
                                                 parent_data=process.top_pipeline.data)
            return HandleResult(next_node=None, should_return=True, should_sleep=True)

        process.top_pipeline.context().extract_output(loop_service_act)
        if not Status.objects.finish(loop_service_act):
            # has been forced failed

            # ignore_error have been called
            if error_occurred:
                loop_service_act.revert_ignore_error()

            LoopActivityHistory.objects.record(loop_service_act)
            return HandleResult(next_node=None, should_return=False, should_sleep=True)

        LoopActivityHistory.objects.record(loop_service_act)
        loop_service_act.loop_success()
        LoopActivityStatus.objects.refresh_status(loop_service_act)
        return HandleResult(next_node=loop_service_act.next(), should_return=False, should_sleep=False)


def service_activity_handler(process, service_act):
    success = False
    exception_occurred = False
    monitoring = False
    version = Status.objects.get(id=service_act.id).version
    root_pipeline = process.root_pipeline

    # rerun mode
    if Status.objects.get(id=service_act.id).loop > 1:
        service_act.prepare_rerun_data()

    # hydrate inputs
    hydrate_node_data(service_act)

    if service_act.timeout:
        logger.info('node %s %s start timeout monitor, timeout: %s' % (service_act.id, version, service_act.timeout))
        signals.service_activity_timeout_monitor_start.send(sender=service_act.__class__,
                                                            node_id=service_act.id,
                                                            version=version,
                                                            root_pipeline_id=root_pipeline.id,
                                                            countdown=service_act.timeout)
        monitoring = True

    # execute service
    try:
        success = service_act.execute(root_pipeline.data)
    except Exception as e:
        if service_act.error_ignorable:
            # ignore exception
            success = True
            exception_occurred = True
            service_act.ignore_error()
        else:
            # send activity error signal
            valve.send(signals, 'activity_failed',
                       sender=root_pipeline,
                       pipeline_id=root_pipeline.id,
                       pipeline_activity_id=service_act.id)
        ex_data = traceback.format_exc(e)
        service_act.data.set_outputs('ex_data', ex_data)
        logger.error(ex_data)

    # process result
    if success is False:
        ex_data = service_act.data.get_one_of_outputs('ex_data')
        Status.objects.fail(service_act, ex_data)
        try:
            service_act.failure_handler(root_pipeline.data)
        except Exception as e:
            logger.error('failure_handler(%s) failed: %s' % (service_act.id, traceback.format_exc(e)))

        if monitoring:
            signals.service_activity_timeout_monitor_end.send(sender=service_act.__class__,
                                                              node_id=service_act.id,
                                                              version=version)
            logger.info('node %s %s timeout monitor revoke' % (service_act.id, version))

        # send activity error signal
        valve.send(signals, 'activity_failed', sender=root_pipeline,
                   pipeline_id=root_pipeline.id,
                   pipeline_activity_id=service_act.id)

        return HandleResult(next_node=None, should_return=False, should_sleep=True)
    else:
        is_error_ignored = service_act.error_ignorable and not service_act.get_result_bit()
        if service_act.need_schedule() and not exception_occurred and not is_error_ignored:
            # write data before schedule
            Data.objects.write_node_data(service_act)
            # set schedule
            ScheduleService.objects.set_schedule(service_act.id,
                                                 service_act=service_act.shell(),
                                                 process_id=process.id,
                                                 version=version,
                                                 parent_data=process.top_pipeline.data)
            return HandleResult(next_node=None, should_return=True, should_sleep=True)

        process.top_pipeline.context().extract_output(service_act)
        error_ignorable = not service_act.get_result_bit()

        if monitoring:
            signals.service_activity_timeout_monitor_end.send(sender=service_act.__class__,
                                                              node_id=service_act.id,
                                                              version=version)
            logger.info('node %s %s timeout monitor revoke' % (service_act.id, version))

        if not Status.objects.finish(service_act, error_ignorable):
            # has been forced failed
            return HandleResult(next_node=None, should_return=False, should_sleep=True)
        return HandleResult(next_node=service_act.next(), should_return=False, should_sleep=False)


def subprocess_handler(process, subprocess_act):
    # hydrate data
    hydrate_node_data(subprocess_act)

    # context injection
    data = subprocess_act.pipeline.data
    context = subprocess_act.pipeline.context()
    for k, v in data.get_inputs().items():
        context.set_global_var(k, v)

    hydrated = hydrate_data(context.variables)
    context.update_global_var(hydrated)

    sub_pipeline = subprocess_act.pipeline
    process.push_pipeline(sub_pipeline, is_subprocess=True)
    return HandleResult(next_node=sub_pipeline.start_event(), should_return=False, should_sleep=False)


def parallel_gateway_handler(process, parallel_gateway):
    targets = parallel_gateway.outgoing.all_target_node()
    children = []

    for target in targets:
        try:
            child = PipelineProcess.objects.fork_child(parent=process,
                                                       current_node_id=target.id,
                                                       destination_id=parallel_gateway.converge_gateway_id)
        except PipelineException as e:
            logger.error(traceback.format_exc(e))
            Status.objects.fail(parallel_gateway, e.message)
            return HandleResult(next_node=None, should_return=True, should_sleep=True)

        children.append(child)

    process.join(children)

    Status.objects.finish(parallel_gateway)

    return HandleResult(next_node=None, should_return=True, should_sleep=True)


def empty_end_event_handler(process, end_event):
    pipeline = process.pop_pipeline()
    if process.pipeline_stack:
        # pop subprocess and return to top of stack
        pipeline.spec.context.write_output(pipeline)
        Status.objects.finish(end_event)
        sub_process_node = process.top_pipeline.node(pipeline.id)
        Status.objects.finish(sub_process_node)
        pipeline.context().clear()
        # extract subprocess output
        process.top_pipeline.context().extract_output(sub_process_node)
        return HandleResult(next_node=sub_process_node.next(), should_return=False, should_sleep=False)
    else:
        with Status.objects.lock(pipeline.id):
            # save data and destroy process
            pipeline.spec.context.write_output(pipeline)
            Data.objects.write_node_data(pipeline)
            Status.objects.finish(end_event)

            Status.objects.transit(pipeline.id, to_state=states.FINISHED, is_pipeline=True)
            # PipelineInstance.objects.set_finished(process.root_pipeline.id)
            end_event.pipeline_finish(process.root_pipeline.id)
            pipeline.context().clear()
            process.destroy()
            return HandleResult(next_node=None, should_return=True, should_sleep=False)


def empty_start_event_handler(process, start_event):
    Status.objects.finish(start_event)
    return HandleResult(next_node=start_event.next(), should_return=False, should_sleep=False)


def exclusive_gateway_handler(process, ex_gateway):
    try:
        hydrate_context = hydrate_data(process.top_pipeline.context().variables)
        next_node = ex_gateway.next(hydrate_context)
    except PipelineException as e:
        logger.error(traceback.format_exc(e))
        Status.objects.fail(ex_gateway, ex_data=e.message)
        return HandleResult(next_node=None, should_return=True, should_sleep=True)
    Status.objects.finish(ex_gateway)
    return HandleResult(next_node=next_node, should_return=False, should_sleep=False)


def converge_gateway_handler(process, converge_gateway):
    # try to sync data if current process has children
    if process.children:
        try:
            process.sync_with_children()
        except exceptions.ChildDataSyncError as e:
            logger.error(traceback.format_exc(e))
            # clean children and update current_node to prevent re execute child process
            process.clean_children()
            Status.objects.fail(converge_gateway,
                                ex_data='Sync branch context error, check data backend status please.')
            return HandleResult(next_node=None, should_return=True, should_sleep=True)

    Status.objects.finish(converge_gateway)
    return HandleResult(next_node=converge_gateway.next(), should_return=False, should_sleep=False)


FLOW_NODE_HANDLERS = {
    event.EmptyStartEvent: empty_start_event_handler,
    event.EmptyEndEvent: empty_end_event_handler,
    activity.ServiceActivity: service_activity_handler,
    activity.SubProcess: subprocess_handler,
    gateway.ExclusiveGateway: exclusive_gateway_handler,
    gateway.ParallelGateway: parallel_gateway_handler,
    gateway.ConvergeGateway: converge_gateway_handler,
    activity.LoopServiceActivity: loop_service_activity_handler
}
