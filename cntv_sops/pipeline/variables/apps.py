# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.db.utils import ProgrammingError

from pipeline.conf import settings
from pipeline.utils.register import autodiscover_collections


class VariablesConfig(AppConfig):
    name = 'pipeline.variables'
    verbose_name = 'PipelineVariables'

    def ready(self):
        """
        @summary: 注册公共部分和RUN_VER下的变量到数据库
        @return:
        """
        for path in settings.VARIABLE_AUTO_DISCOVER_PATH:
            autodiscover_collections(path)

        from pipeline.models import VariableModel
        from pipeline.core.data.library import VariableLibrary
        try:
            VariableModel.objects.exclude(code__in=VariableLibrary.variables.keys()).update(status=False)
        except ProgrammingError:
            # first migrate
            pass
