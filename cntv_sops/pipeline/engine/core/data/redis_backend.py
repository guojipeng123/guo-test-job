# -*- coding: utf-8 -*-
try:
    import cPickle as pickle
except Exception:
    import pickle

from pipeline.conf import settings
from pipeline.engine.core.data.base_backend import BaseDataBackend


class RedisDataBackend(BaseDataBackend):

    def set_object(self, key, obj):
        return settings.redis_inst.set(key, pickle.dumps(obj))

    def get_object(self, key):
        pickle_str = settings.redis_inst.get(key)
        if not pickle_str:
            return None
        return pickle.loads(pickle_str)

    def del_object(self, key):
        return settings.redis_inst.delete(key)

    def expire_cache(self, key, value, expires):
        settings.redis_inst.set(key, pickle.dumps(value))
        settings.redis_inst.expire(key, expires)
        return True

    def cache_for(self, key):
        cache = settings.redis_inst.get(key)
        return pickle.loads(cache) if cache else cache
