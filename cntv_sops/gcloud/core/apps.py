# -*- coding: utf-8 -*-
import logging
import traceback

from django.apps import AppConfig
from django.conf import settings


logger = logging.getLogger('root')


class CoreConfig(AppConfig):
    name = 'gcloud.core'
    verbose_name = 'GcloudCore'

    def ready(self):
        from gcloud.core.signals.handlers import business_post_save_handler  # noqa
        if not hasattr(settings, 'REDIS'):
            try:
                from gcloud.core.models import EnvironmentVariables
                settings.REDIS = {
                    'host': EnvironmentVariables.objects.get_var('BKAPP_REDIS_HOST'),
                    'port': EnvironmentVariables.objects.get_var('BKAPP_REDIS_PORT'),
                    'password': EnvironmentVariables.objects.get_var('BKAPP_REDIS_PASSWORD'),
                    'service_name': EnvironmentVariables.objects.get_var('BKAPP_REDIS_SERVICE_NAME'),
                    'mode': EnvironmentVariables.objects.get_var('BKAPP_REDIS_MODE')
                }
            except Exception:
                logger.error(traceback.format_exc())
