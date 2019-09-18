# -*- coding: utf-8 -*-
from collections import namedtuple
from django.utils import timezone


class Stack(list):
    def top(self):
        return self[len(self) - 1]

    def push(self, item):
        self.append(item)


class ConstantDict(dict):
    """ConstantDict is a subclass of :class:`dict`, implementing __setitem__
    method to avoid item assignment::

    >>> d = ConstantDict({'key': 'value'})
    >>> d['key'] = 'value'
    Traceback (most recent call last):
        ...
    TypeError: 'ConstantDict' object does not support item assignment
    """

    def __setitem__(self, key, value):
        raise TypeError("'%s' object does not support item assignment"
                        % self.__class__.__name__)


def calculate_elapsed_time(started_time, archived_time):
    """
    @summary: 计算节点耗时
    @param started_time: 执行开始时间
    @param archived_time: 执行结束时间
    @return:
    """
    if archived_time and started_time:
        # when status_tree['archived_time'] == status_tree['started_time'], set elapsed_time to 1s
        elapsed_time = (archived_time - started_time).seconds or 1
    elif started_time:
        elapsed_time = (timezone.now() - started_time).seconds
    else:
        elapsed_time = 0
    return elapsed_time


ActionResult = namedtuple('ActionResult', 'result message')
