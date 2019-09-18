# -*- coding: utf-8 -*-
from django.apps import AppConfig


class PeriodicTaskConfig(AppConfig):
    name = 'pipeline.contrib.periodic_task'
    verbose_name = 'PipelinePeriodicTask'

    def ready(self):
        pass
