# -*- coding: utf-8 -*-


from django.apps import AppConfig


class LogConfig(AppConfig):
    name = 'pipeline.log'
    verbose_name = "Database Logging"

    def ready(self):
        from pipeline.log import setup
        setup()
