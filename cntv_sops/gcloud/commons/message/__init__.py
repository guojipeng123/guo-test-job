# -*- coding: utf-8 -*-
import importlib
import json

from django.conf import settings

from gcloud.commons.message.common import (title_and_content_for_atom_failed,
                                           title_and_content_for_flow_finished,
                                           title_and_content_for_periodic_task_start_fail)

_message_module = importlib.import_module('gcloud.commons.message.sites.%s.send_msg' % settings.RUN_VER)

ATOM_FAILED = 'atom_failed'
TASK_FINISHED = 'task_finished'


def send_task_flow_message(taskflow, msg_type, atom_node_name=''):
    template = taskflow.template
    pipeline_inst = taskflow.pipeline_instance
    executor = pipeline_inst.executor

    notify_type = json.loads(template.notify_type)
    receivers_list = template.get_notify_receivers_list(executor)
    receivers = ','.join(receivers_list)

    if msg_type == 'atom_failed':
        title, content = title_and_content_for_atom_failed(taskflow, pipeline_inst, atom_node_name, executor)
    elif msg_type == 'task_finished':
        title, content = title_and_content_for_flow_finished(taskflow, pipeline_inst, atom_node_name, executor)
    else:
        return False

    _message_module.send_message(taskflow.business.cc_id, executor, notify_type, receivers, title, content)

    return True


def send_periodic_task_message(template, periodic_task, history):
    notify_type = json.loads(template.notify_type)
    receivers_list = template.get_notify_receivers_list(periodic_task.creator)
    receivers = ','.join(receivers_list)

    title, content = title_and_content_for_periodic_task_start_fail(template, periodic_task, history)

    _message_module.send_message(template.business.cc_id, periodic_task.creator, notify_type, receivers, title, content)

    return True
