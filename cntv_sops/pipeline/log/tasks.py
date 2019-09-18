# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

from django.conf import settings
from celery.schedules import crontab
from celery.decorators import periodic_task


from pipeline.log.models import LogEntry


logger = logging.getLogger(__name__)


@periodic_task(run_every=(crontab(minute=0, hour=0)), ignore_result=True)
def clean_expired_log():
    expired_interval = getattr(settings, 'LOG_PERSISTENT_DAYS', None)

    if expired_interval is None:
        expired_interval = 30
        logger.warning('LOG_PERSISTENT_DAYS are not found in settings, use default value: 30')

    del_num = LogEntry.objects.delete_expired_log(expired_interval)
    logger.info('%s log entry are deleted' % del_num)
