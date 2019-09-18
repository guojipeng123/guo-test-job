# -*- coding: utf-8 -*-
from pipeline.utils.uniqid import uniqid
from pipeline.core.constants import PE

__all__ = [
    'Element',
    'PE'
]


class Element(object):
    def __init__(self, id=None, name=None, outgoing=None):
        self.id = id or uniqid()
        self.name = name
        self.outgoing = outgoing or []

    def extend(self, element):
        self.outgoing.append(element)
        return element

    def connect(self, *args):
        for e in args:
            self.outgoing.append(e)
        return self

    def converge(self, element):
        for e in self.outgoing:
            e.tail().connect(element)
        return element

    def to(self, element):
        return element

    def tail(self):
        is_tail = len(self.outgoing) == 0
        e = self

        while not is_tail:
            e = e.outgoing[0]
            is_tail = len(e.outgoing) == 0

        return e

    def type(self):
        raise NotImplementedError()

    def __eq__(self, other):
        return self.id == other.id
