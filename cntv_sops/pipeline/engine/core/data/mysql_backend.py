# -*- coding: utf-8 -*-

from django.core.cache import cache

from pipeline.engine.core.data.base_backend import BaseDataBackend
from pipeline.engine.models.data import DataSnapshot


class MySQLDataBackend(BaseDataBackend):

    def set_object(self, key, obj):
        return DataSnapshot.objects.set_object(key, obj)

    def get_object(self, key):
        return DataSnapshot.objects.get_object(key)

    def del_object(self, key):
        return DataSnapshot.objects.del_object(key)

    def expire_cache(self, key, value, expires):
        return cache.set(key, value, expires)

    def cache_for(self, key):
        return cache.get(key)
