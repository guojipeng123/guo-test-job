# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging


def get_pipeline_logger():
    return logging.getLogger(__name__)


pipeline_logger = get_pipeline_logger()
