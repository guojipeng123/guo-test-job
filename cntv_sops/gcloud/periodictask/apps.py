# -*- coding: utf-8 -*-
from django.apps import AppConfig


class PeriodicTaskConfig(AppConfig):
    name = 'gcloud.periodictask'
    verbose_name = 'GcloudPeriodicTask'

    def ready(self):
        from gcloud.periodictask.signals.handlers import *  # noqa
