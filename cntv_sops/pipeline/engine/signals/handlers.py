# -*- coding: utf-8 -*-

from pipeline.engine import tasks, hooks
from pipeline.engine.models import ProcessCeleryTask, ScheduleCeleryTask, NodeCeleryTask


def pipeline_ready_handler(sender, process_id, **kwargs):
    ProcessCeleryTask.objects.start_task(
        process_id=process_id,
        start_func=tasks.start.apply_async,
        kwargs={
            'args': [process_id]
        }
    )


def child_process_ready_handler(sender, child_id, **kwargs):
    ProcessCeleryTask.objects.start_task(
        process_id=child_id,
        start_func=tasks.dispatch.apply_async,
        kwargs={
            'args': [child_id]
        }
    )


def process_ready_handler(sender, process_id, current_node_id=None, call_from_child=False, **kwargs):
    ProcessCeleryTask.objects.start_task(
        process_id=process_id,
        start_func=tasks.process_wake_up.apply_async,
        kwargs={
            'args': [process_id, current_node_id, call_from_child]
        }
    )


def batch_process_ready_handler(sender, process_id_list, pipeline_id, **kwargs):
    tasks.batch_wake_up.apply_async(args=[process_id_list, pipeline_id])


def wake_from_schedule_handler(sender, process_id, activity_id, **kwargs):
    ProcessCeleryTask.objects.start_task(
        process_id=process_id,
        start_func=tasks.wake_from_schedule.apply_async,
        kwargs={
            'args': [process_id, activity_id]
        }
    )


def process_unfreeze_handler(sender, process_id, **kwargs):
    ProcessCeleryTask.objects.start_task(
        process_id=process_id,
        start_func=tasks.process_unfreeze.apply_async,
        kwargs={
            'args': [process_id]
        }
    )


def schedule_ready_handler(sender, process_id, schedule_id, countdown, **kwargs):
    ScheduleCeleryTask.objects.start_task(
        schedule_id=schedule_id,
        start_func=tasks.service_schedule.apply_async,
        kwargs={
            'args': [process_id, schedule_id],
            'countdown': countdown
        }
    )


def schedule_success_handler(sender, activity_shell, schedule_service, **kwargs):
    cls = activity_shell.__class__
    h = hooks.schedule_success_hooks
    if cls in h:
        h[cls](activity_shell, schedule_service)


def schedule_fail_handler(sender, activity_shell, schedule_service, ex_data, **kwargs):
    cls = activity_shell.__class__
    h = hooks.schedule_failed_hooks
    if cls in h:
        h[cls](activity_shell, schedule_service, ex_data)


def node_skip_call_handler(sender, process, node, **kwargs):
    cls = node.__class__
    h = hooks.node_skip_call_hooks
    if cls in h:
        h[cls](process, node)


def node_retry_ready_handler(sender, process, node, **kwargs):
    cls = node.__class__
    h = hooks.node_retry_ready_hooks
    if cls in h:
        h[cls](process, node)


def service_activity_timeout_monitor_start_handler(sender, node_id, version, root_pipeline_id, countdown, **kwargs):
    NodeCeleryTask.objects.start_task(
        node_id=node_id,
        start_func=tasks.node_timeout_check.apply_async,
        kwargs={
            'args': [node_id, version, root_pipeline_id],
            'countdown': countdown
        }
    )


def service_activity_timeout_monitor_end_handler(sender, node_id, version, **kwargs):
    NodeCeleryTask.objects.revoke(node_id)
