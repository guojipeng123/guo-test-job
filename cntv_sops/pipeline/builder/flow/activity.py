# -*- coding: utf-8 -*-
from pipeline.builder.flow.base import *  # noqa
from pipeline.utils.collections import FancyDict

__all__ = [
    'ServiceActivity',
    'SubProcess'
]


class ServiceActivity(Element):
    def __init__(self, component_code=None, *args, **kwargs):
        self.component = FancyDict({
            'code': component_code,
            'global_outputs': FancyDict({}),
            'inputs': FancyDict({})
        })
        super(ServiceActivity, self).__init__(*args, **kwargs)

    def type(self):
        return PE.ServiceActivity

    def add_output(self, source, target):
        self.component.global_outputs[source] = target

    def del_output(self, source):
        del self.component.global_outputs[source]

    def component_dict(self):
        return {
            'code': self.component.code,
            'global_outputs': self.component.global_outputs,
            'inputs': {key: var.to_dict() for key, var in self.component.inputs.items()}
        }


class SubProcess(Element):

    def __init__(self, start, data=None, params=None, *args, **kwargs):
        self.start = start
        self.data = data
        self.params = params or {}
        super(SubProcess, self).__init__(*args, **kwargs)

    def type(self):
        return PE.SubProcess
