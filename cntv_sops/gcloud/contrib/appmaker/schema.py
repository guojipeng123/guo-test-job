# -*- coding: utf-8 -*-

APP_MAKER_PARAMS_SCHEMA = {
    'type': 'object',
    'required': ['id', 'template_id', 'name'],
    'properties': {
        'id': {
            'type': 'string',
        },
        'template_id': {
            'type': 'string',
        },
        'name': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 20,
        },
    }
}
