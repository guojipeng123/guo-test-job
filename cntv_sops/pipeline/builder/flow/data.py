# -*- coding: utf-8 -*-
from pipeline.core.constants import PE
from pipeline.utils.collections import FancyDict


class Data(object):
    def __init__(self):
        self.inputs = FancyDict({})
        self.outputs = FancyDict({})


class Var(object):
    PLAIN = PE.plain
    SPLICE = PE.splice
    LAZY = PE.lazy

    def __init__(self, type, value, source_tag=None):
        self.type = type
        self.value = value
        self.source_tag = source_tag

    def to_dict(self):
        base = {
            'type': self.type,
            'value': self.value
        }
        if self.type == self.LAZY:
            base['source_tag'] = self.source_tag

        return base


class DataInput(Var):

    def __init__(self, is_param, *args, **kwargs):
        self.is_param = is_param
        super(DataInput, self).__init__(*args, **kwargs)
