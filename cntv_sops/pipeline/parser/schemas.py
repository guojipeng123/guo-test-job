# -*- coding: utf-8 -*-

PIPELINE_TREE_PARSER = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "inputs": {
                    "type": "object"
                },
                "outputs": {
                    "type": "object"
                }
            }
        },
        "activities": {
            "type": "object"
        },
        "end_event": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "incoming": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "outgoing": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                }
            }
        },
        "flows": {
            "type": "object"
        },
        "gateways": {
            "type": "object"
        },
        "id": {
            "type": "string"
        },
        "line": {
            "type": "array"
        },
        "location": {
            "type": "array"
        },
        "start_event": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "incoming": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "outgoing": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                }
            }
        }
    }
}
