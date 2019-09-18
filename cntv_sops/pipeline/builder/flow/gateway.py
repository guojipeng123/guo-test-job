# -*- coding: utf-8 -*-
from pipeline.builder.flow.base import *  # noqa

__all__ = [
    'ParallelGateway',
    'ExclusiveGateway',
    'ConvergeGateway'
]


class ParallelGateway(Element):

    def type(self):
        return PE.ParallelGateway


class ExclusiveGateway(Element):

    def __init__(self, conditions=None, *args, **kwargs):
        self.conditions = conditions or {}
        super(ExclusiveGateway, self).__init__(*args, **kwargs)

    def add_condition(self, index, evaluate):
        self.conditions[index] = evaluate

    def link_conditions_with(self, outgoing):
        conditions = {}
        for i, out in enumerate(outgoing):
            conditions[out] = {PE.evaluate: self.conditions[i]}

        return conditions

    def type(self):
        return PE.ExclusiveGateway


class ConvergeGateway(Element):

    def type(self):
        return PE.ConvergeGateway
