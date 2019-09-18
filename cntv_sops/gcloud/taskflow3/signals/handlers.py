# -*- coding: utf-8 -*-

import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from gcloud.taskflow3.models import TaskFlowInstance
from gcloud.taskflow3.signals import taskflow_finished
from gcloud.commons.message import send_task_flow_message, ATOM_FAILED, TASK_FINISHED
from pipeline.models import PipelineInstance

logger = logging.getLogger('celery')


@receiver(post_save, sender=PipelineInstance)
def pipeline_post_save_handler(sender, instance, created, **kwargs):
    if not created and instance.is_finished:
        try:
            taskflow = TaskFlowInstance.objects.get(pipeline_instance=instance)
        except TaskFlowInstance.DoesNotExist:
            logger.error(u"pipeline finished handler get taskflow error, pipeline_instance_id=%s" % instance.id)
            return
        if taskflow.current_flow != 'finished':
            taskflow.current_flow = 'finished'
            taskflow.save()
            taskflow_finished.send(sender=taskflow, username=taskflow.pipeline_instance.executor)


def taskflow_node_failed_handler(sender, pipeline_id, pipeline_activity_id, **kwargs):
    try:
        taskflow = TaskFlowInstance.objects.get(pipeline_instance__instance_id=pipeline_id)
    except TaskFlowInstance.DoesNotExist:
        logger.error(u"pipeline finished handler get taskflow error, pipeline_instance_id=%s" % pipeline_id)
        return

    try:
        activity_name = taskflow.get_act_web_info(pipeline_activity_id)['name']
        send_task_flow_message(taskflow, ATOM_FAILED, activity_name)
    except Exception as e:
        logger.error('taskflow_node_failed_handler[taskflow_id=%s] send message error: %s' % (taskflow.id, e))
    return


@receiver(taskflow_finished)
def taskflow_finished_handler(sender, username, **kwargs):
    try:
        taskflow = sender
        send_task_flow_message(taskflow, TASK_FINISHED)
    except Exception as e:
        logger.error('taskflow_finished_handler[taskflow_id=%s] send message error: %s' % (taskflow.id, e))
    return
