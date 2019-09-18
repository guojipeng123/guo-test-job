# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta


class BaseDataBackend(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_object(self, key, obj):
        raise NotImplementedError()

    @abstractmethod
    def get_object(self, key):
        raise NotImplementedError()

    @abstractmethod
    def del_object(self, key):
        raise NotImplementedError()

    @abstractmethod
    def expire_cache(self, key, value, expires):
        raise NotImplementedError()

    @abstractmethod
    def cache_for(self, key):
        raise NotImplementedError()
