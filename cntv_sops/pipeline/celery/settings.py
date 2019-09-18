from kombu import Exchange, Queue

default_exchange = Exchange('default', type='direct')

PIPELINE_ROUTING = {
    'queue': 'pipeline',
    'routing_key': 'pipeline_push'
}

PIPELINE_ADDITIONAL_ROUTING = {
    'queue': 'pipeline_additional_task',
    'routing_key': 'additional_task'
}

CELERY_ROUTES = {
    # schedule
    'pipeline.engine.tasks.service_schedule': {
        'queue': 'service_schedule',
        'routing_key': 'schedule_service'
    },
    # pipeline
    'pipeline.engine.tasks.batch_wake_up': PIPELINE_ROUTING,
    'pipeline.engine.tasks.dispatch': PIPELINE_ROUTING,
    'pipeline.engine.tasks.process_wake_up': PIPELINE_ROUTING,
    'pipeline.engine.tasks.start': PIPELINE_ROUTING,
    'pipeline.engine.tasks.wake_from_schedule': PIPELINE_ROUTING,
    'pipeline.engine.tasks.wake_up': PIPELINE_ROUTING,
    'pipeline.engine.tasks.process_unfreeze': PIPELINE_ROUTING,
    # another
    'pipeline.log.tasks.clean_expired_log': PIPELINE_ADDITIONAL_ROUTING,
    'pipeline.engine.tasks.node_timeout_check': PIPELINE_ADDITIONAL_ROUTING,
    'pipeline.contrib.periodic_task.tasks.periodic_task_start': PIPELINE_ADDITIONAL_ROUTING,
}

CELERY_QUEUES = (
    Queue('pipeline', default_exchange, routing_key='pipeline_push'),
    Queue('service_schedule', default_exchange, routing_key='schedule_service'),
    Queue('pipeline_additional_task', default_exchange, routing_key='additional_task')
)

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'
