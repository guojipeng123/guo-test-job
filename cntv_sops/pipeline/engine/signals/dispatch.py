# -*- coding: utf-8 -*-

from pipeline.core.pipeline import Pipeline
from pipeline.core.flow.activity import ServiceActivity
from pipeline.engine import models
from pipeline.engine import signals
from pipeline.engine.signals import handlers


# DISPATCH_UID = __name__.replace('.', '_')


def dispatch_pipeline_ready():
    signals.pipeline_ready.connect(
        handlers.pipeline_ready_handler,
        sender=Pipeline,
        dispatch_uid='_pipeline_ready'
    )


def dispatch_child_process_ready():
    signals.child_process_ready.connect(
        handlers.child_process_ready_handler,
        sender=models.PipelineProcess,
        dispatch_uid='_child_process_ready'
    )


def dispatch_process_ready():
    signals.process_ready.connect(
        handlers.process_ready_handler,
        sender=models.PipelineProcess,
        dispatch_uid='_process_ready'
    )


def dispatch_batch_process_ready():
    signals.batch_process_ready.connect(
        handlers.batch_process_ready_handler,
        sender=models.PipelineProcess,
        dispatch_uid='_batch_process_ready'
    )


def dispatch_wake_from_schedule():
    signals.wake_from_schedule.connect(
        handlers.wake_from_schedule_handler,
        sender=models.ScheduleService,
        dispatch_uid='_wake_from_schedule'
    )


def dispatch_schedule_ready():
    signals.schedule_ready.connect(
        handlers.schedule_ready_handler,
        sender=models.ScheduleService,
        dispatch_uid='_schedule_ready'
    )


def dispatch_process_unfreeze():
    signals.process_unfreeze.connect(
        handlers.process_unfreeze_handler,
        sender=models.PipelineProcess,
        dispatch_uid='_process_unfreeze'
    )


def dispatch_service_schedule_success():
    signals.service_schedule_success.connect(
        handlers.schedule_success_handler,
        sender=models.ScheduleService,
        dispatch_uid='_service_schedule_success'
    )


def dispatch_service_schedule_fail():
    signals.service_schedule_fail.connect(
        handlers.schedule_fail_handler,
        sender=models.ScheduleService,
        dispatch_uid='_service_schedule_fail'
    )


def dispatch_node_skip_call():
    signals.node_skip_call.connect(
        handlers.node_skip_call_handler,
        sender=models.Status,
        dispatch_uid='_node_skip_call'
    )


def dispatch_node_retry_ready():
    signals.node_retry_ready.connect(
        handlers.node_retry_ready_handler,
        sender=models.Status,
        dispatch_uid='_node_retry_ready'
    )


def dispatch_service_activity_timeout_monitor_start():
    signals.service_activity_timeout_monitor_start.connect(
        handlers.service_activity_timeout_monitor_start_handler,
        sender=ServiceActivity,
        dispatch_uid='_service_activity_timeout_monitor_start'
    )


def dispatch_service_activity_timeout_monitor_end():
    signals.service_activity_timeout_monitor_end.connect(
        handlers.service_activity_timeout_monitor_end_handler,
        sender=ServiceActivity,
        dispatch_uid='__service_activity_timeout_monitor_end'
    )


def dispatch():
    dispatch_pipeline_ready()
    dispatch_child_process_ready()
    dispatch_process_ready()
    dispatch_batch_process_ready()
    dispatch_wake_from_schedule()
    dispatch_schedule_ready()
    dispatch_process_unfreeze()
    dispatch_service_schedule_success()
    dispatch_service_schedule_fail()
    dispatch_node_skip_call()
    dispatch_node_retry_ready()
    dispatch_service_activity_timeout_monitor_start()
    dispatch_service_activity_timeout_monitor_end()
