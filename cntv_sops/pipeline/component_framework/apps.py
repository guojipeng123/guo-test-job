# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.db.utils import ProgrammingError

from pipeline.conf import settings
from pipeline.utils.register import autodiscover_collections


class ComponentFrameworkConfig(AppConfig):
    name = 'pipeline.component_framework'
    verbose_name = 'PipelineComponentFramework'

    def ready(self):
        """
        @summary: 注册公共部分和当前RUN_VER下的原子到数据库
        @return:
        """

        for path in settings.COMPONENT_AUTO_DISCOVER_PATH:
            autodiscover_collections(path)

        from pipeline.component_framework.models import ComponentModel
        from pipeline.component_framework.library import ComponentLibrary
        try:
            ComponentModel.objects.exclude(code__in=ComponentLibrary.components.keys()).update(status=False)
        except ProgrammingError:
            # first migrate
            pass
