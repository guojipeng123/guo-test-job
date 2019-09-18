# -*- coding: utf-8 -*-

import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from gcloud.taskflow3.models import TaskFlowInstance
from gcloud.tasktmpl3.models import TaskTemplate
from gcloud.periodictask.models import PeriodicTaskHistory
from gcloud.commons.message import send_periodic_task_message
from pipeline.contrib.periodic_task.models import PeriodicTaskHistory as PipelinePeriodicTaskHistory
from pipeline.contrib.periodic_task.models import PeriodicTask as PipelinePeriodicTask
from pipeline.contrib.periodic_task.signals import pre_periodic_task_start, periodic_task_start_failed

logger = logging.getLogger('celery')


@receiver(pre_periodic_task_start, sender=PipelinePeriodicTask)
def pre_periodic_task_start_handler(sender, periodic_task, pipeline_instance, **kwargs):
    TaskFlowInstance.objects.create(
        business_id=periodic_task.extra_info['business_id'],
        pipeline_instance=pipeline_instance,
        category=periodic_task.extra_info['category'],
        template_id=periodic_task.extra_info['template_num_id'],
        create_method='periodic',
        create_info='',
        flow_type='common',
        current_flow='execute_task'
    )


@receiver(post_save, sender=PipelinePeriodicTaskHistory)
def periodic_task_history_post_save_handler(sender, instance, created, **kwargs):
    if created:
        PeriodicTaskHistory.objects.record_history(instance)


@receiver(periodic_task_start_failed, sender=PipelinePeriodicTask)
def periodic_task_start_failed_handler(sender, periodic_task, history, **kwargs):
    extra_info = periodic_task.extra_info
    try:
        template = TaskTemplate.objects.get(business_id=extra_info['business_id'],
                                            id=extra_info['template_num_id'])
        send_periodic_task_message(template, periodic_task, history)
    except Exception as e:
        logger.error('periodic_task_start_failed_handler[template_id=%s] send message error: %s' %
                     (extra_info['template_num_id'], e))
