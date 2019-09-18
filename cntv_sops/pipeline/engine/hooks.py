# -*- coding: utf-8 -*-
from pipeline.core.flow import activity
from pipeline.engine.models import (LoopActivityHistory,
                                    LoopActivityStatus,
                                    LoopActivityScheduleHistory,
                                    ScheduleService,
                                    PipelineProcess)


def loop_service_activity_schedule_success(loop_service_act, schedule_service):
    # change loop state
    loop_service_act.loop_success()

    process = PipelineProcess.objects.get(current_node_id=loop_service_act.id)
    real_act = process.top_pipeline.node(loop_service_act.id)
    real_act.loop_success()
    process.save()

    schedule = LoopActivityScheduleHistory.objects.record(loop_service_act, schedule_service)
    LoopActivityHistory.objects.record(loop_service_act, schedule=schedule)
    LoopActivityStatus.objects.refresh_status(loop_service_act)
    ScheduleService.objects.delete_schedule(schedule_service.activity_id, schedule_service.version)


def loop_service_activity_schedule_fail(loop_service_act, schedule_service, ex_data):

    process = PipelineProcess.objects.get(current_node_id=loop_service_act.id)
    real_act = process.top_pipeline.node(loop_service_act.id)
    real_act.data.set_outputs('ex_data', ex_data)
    process.save()

    loop_service_act.data.set_outputs('ex_data', ex_data)
    schedule = LoopActivityScheduleHistory.objects.record(loop_service_act, schedule_service)
    LoopActivityHistory.objects.record(loop_service_act, schedule=schedule)
    ScheduleService.objects.delete_schedule(schedule_service.activity_id, schedule_service.version)


def loop_service_activity_skip(process, node):
    LoopActivityStatus.objects.refresh_status(node)


def loop_service_activity_retry(process, node):
    setattr(node, 'retrying', True)


schedule_success_hooks = {
    activity.LoopServiceActivity: loop_service_activity_schedule_success
}

schedule_failed_hooks = {
    activity.LoopServiceActivity: loop_service_activity_schedule_fail
}

node_skip_call_hooks = {
    activity.LoopServiceActivity: loop_service_activity_skip
}

node_retry_ready_hooks = {
    activity.LoopServiceActivity: loop_service_activity_retry
}
