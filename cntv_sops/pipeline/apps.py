# -*- coding: utf-8 -*-
from __future__ import absolute_import

import redis
import logging
import traceback

from redis.sentinel import Sentinel
from django.apps import AppConfig
from django.conf import settings
from rediscluster import StrictRedisCluster

logger = logging.getLogger('root')


def get_client_through_sentinel():
    kwargs = {}
    if 'password' in settings.REDIS:
        kwargs['password'] = settings.REDIS['password']
    rs = Sentinel([(settings.REDIS['host'], settings.REDIS['port'])], **kwargs)
    # avoid None value in settings.REDIS
    r = rs.master_for(settings.REDIS.get('service_name') or 'mymaster')
    # try to connect master
    r.echo('Hello Redis')
    return r


def get_cluster_client():
    kwargs = {
        'startup_nodes': [{"host": settings.REDIS['host'], "port": settings.REDIS['port']}]
    }
    if 'password' in settings.REDIS:
        kwargs['password'] = settings.REDIS['password']

    r = StrictRedisCluster(**kwargs)
    r.echo('Hello Redis')
    return r


def get_single_client():
    kwargs = {
        'host': settings.REDIS['host'],
        'port': settings.REDIS['port'],
    }
    if 'password' in settings.REDIS:
        kwargs['password'] = settings.REDIS['password']
    if 'db' in settings.REDIS:
        kwargs['db'] = settings.REDIS['db']

    pool = redis.ConnectionPool(**kwargs)
    return redis.StrictRedis(connection_pool=pool)


CLIENT_GETTER = {
    'replication': get_client_through_sentinel,
    'cluster': get_cluster_client,
    'single': get_single_client
}


class PipelineConfig(AppConfig):
    name = 'pipeline'
    verbose_name = 'Pipeline'

    def ready(self):
        from pipeline.signals.handlers import pipeline_template_post_save_handler  # noqa
        from pipeline.patch.djcelery.djcelery_patch import *  # noqa
        # init redis pool
        if hasattr(settings, 'REDIS'):
            mode = settings.REDIS.get('mode') or 'single'
            try:
                settings.redis_inst = CLIENT_GETTER[mode]()
            except Exception as e:
                # fall back to single node mode
                logger.error("redis client init error: %s" % traceback.format_exc(e))
        else:
            logger.error("can not find REDIS in settings!")
