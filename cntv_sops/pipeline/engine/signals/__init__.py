# -*- coding: utf-8 -*-

from django.dispatch import Signal

pipeline_ready = Signal(providing_args=['process_id'])
child_process_ready = Signal(providing_args=['child_id'])
process_ready = Signal(providing_args=['parent_id', 'current_node_id', 'call_from_child'])
batch_process_ready = Signal(providing_args=['process_id_list', 'pipeline_id'])
wake_from_schedule = Signal(providing_args=['process_id, activity_id'])
schedule_ready = Signal(providing_args=['schedule_id', 'countdown', 'process_id'])
process_unfreeze = Signal(providing_args=['process_id'])
# activity failed signal
activity_failed = Signal(providing_args=['pipeline_id', 'pipeline_activity_id'])

# signal for developer (do not use valve to pass them!)
service_schedule_fail = Signal(providing_args=['activity_shell', 'schedule_service', 'ex_data'])
service_schedule_success = Signal(providing_args=['activity_shell', 'schedule_service'])
node_skip_call = Signal(providing_args=['process', 'node'])
node_retry_ready = Signal(providing_args=['process', 'node'])

service_activity_timeout_monitor_start = Signal(providing_args=['node_id', 'version', 'root_pipeline_id', 'countdown'])
service_activity_timeout_monitor_end = Signal(providing_args=['node_id', 'version'])
