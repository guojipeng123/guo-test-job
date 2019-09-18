# -*- coding: utf-8 -*-
from pipeline.builder.flow.base import *  # noqa

__all__ = [
    'EmptyEndEvent',
    'EmptyStartEvent'
]


class EmptyStartEvent(Element):

    def type(self):
        return PE.EmptyStartEvent


class EmptyEndEvent(Element):

    def type(self):
        return PE.EmptyEndEvent
