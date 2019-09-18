# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging


def setup(level=None):
    from pipeline.logging import pipeline_logger as logger
    from pipeline.log.handlers import EngineLogHandler

    if level in logging._levelNames:
        logger.setLevel(level)

    logging._acquireLock()
    try:
        for hdl in logger.handlers:
            if isinstance(hdl, EngineLogHandler):
                break
        else:
            hdl = EngineLogHandler()
            hdl.setLevel(logger.level)
            logger.addHandler(hdl)
    finally:
        logging._releaseLock()


default_app_config = 'pipeline.log.apps.LogConfig'
