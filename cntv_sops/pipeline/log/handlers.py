# -*- coding: utf-8 -*-
import logging

from . import models


class EngineLogHandler(logging.Handler):
    def emit(self, record):
        models.LogEntry.objects.create(
            logger_name=record.name,
            level_name=record.levelname,
            message=self.format(record),
            exception=record.exc_text,
            node_id=record._id
        )
