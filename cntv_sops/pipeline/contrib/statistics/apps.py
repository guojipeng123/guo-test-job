# -*- coding: utf-8 -*-
from django.apps import AppConfig


class StatisticsConfig(AppConfig):
    name = 'pipeline.contrib.statistics'
    verbose_name = 'PipelineContribStatistics'

    def ready(self):
        from pipeline.contrib.statistics.signals.handlers import (  # noqa
            template_post_save_handler,
            pipeline_post_save_handler
        )
