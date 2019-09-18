# -*- coding: utf-8 -*-
import socket

from redis.exceptions import ConnectionError
from djcelery.app import current_app

from django_signal_valve import valve

from pipeline.conf import settings
from pipeline.engine.models import FunctionSwitch, PipelineProcess
from pipeline.engine import signals
from pipeline.engine.core import data
from pipeline.engine.exceptions import RabbitMQConnectionError


def freeze():
    # turn on switch
    FunctionSwitch.objects.freeze_engine()


def unfreeze():
    # turn off switch
    FunctionSwitch.objects.unfreeze_engine()

    # resend signal
    valve.open_valve(signals)

    # unfreeze process
    frozen_process_list = PipelineProcess.objects.filter(is_frozen=True)
    for process in frozen_process_list:
        process.unfreeze()


def workers():
    try:
        worker_list = data.cache_for('__pipeline__workers__')
    except ConnectionError as e:
        raise e

    if not worker_list:
        tries = 0
        try:
            while tries < 2:
                worker_list = current_app.control.ping(timeout=tries + 1)
                if worker_list:
                    break
                tries += 1
        except socket.error as err:
            raise RabbitMQConnectionError(err.message)

        if worker_list:
            data.expire_cache('__pipeline__workers__', worker_list, settings.PIPELINE_WORKER_STATUS_CACHE_EXPIRES)

    return worker_list
