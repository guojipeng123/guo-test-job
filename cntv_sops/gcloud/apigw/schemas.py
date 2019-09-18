# -*- coding: utf-8 -*-
from gcloud.core.constant import TASK_FLOW, PERIOD_TASK_NAME_MAX_LENGTH

APIGW_CREATE_TASK_PARAMS = {
    'type': 'object',
    'required': ['name'],
    'properties': {
        'name': {
            'type': 'string',
            'minLength': 1,
            'maxLength': PERIOD_TASK_NAME_MAX_LENGTH,
        },
        'flow_type': {
            'type': 'string',
            'enum': TASK_FLOW.keys()
        },
        'constants': {
            'type': 'object',
        },
        'exclude_task_nodes_id': {
            'type': 'array',
        }
    }
}

APIGW_CREATE_PERIODIC_TASK_PARAMS = {
    'type': 'object',
    'required': ['name', 'cron'],
    'properties': {
        'name': {
            'type': 'string',
            'minLength': 1,
            'maxLength': PERIOD_TASK_NAME_MAX_LENGTH,
        },
        'cron': {
            'type': 'object'
        },
        'exclude_task_nodes_id': {
            'type': 'array',
        },
        'constants': {
            'type': 'object',
        },
    }
}
