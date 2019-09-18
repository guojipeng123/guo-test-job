# -*- coding: utf-8 -*-

from abc import ABCMeta
from pipeline.core.flow.base import FlowNode
from pipeline.models import PipelineInstance


class Event(FlowNode):
    __metaclass__ = ABCMeta

    def __init__(self, id, name=None, data=None):
        super(Event, self).__init__(id, name, data)

    def next(self):
        return self.outgoing.unique_one().target


class ThrowEvent(Event):
    __metaclass__ = ABCMeta


class CatchEvent(Event):
    __metaclass__ = ABCMeta


class EndEvent(ThrowEvent):
    __metaclass__ = ABCMeta

    def pipeline_finish(self, root_pipeline_id):
        return


class StartEvent(CatchEvent):
    __metaclass__ = ABCMeta


class EmptyStartEvent(StartEvent):
    pass


class EmptyEndEvent(EndEvent):
    def pipeline_finish(self, root_pipeline_id):
        try:
            PipelineInstance.objects.set_finished(root_pipeline_id)
        except PipelineInstance.DoesNotExist:  # task which do not belong to any instance
            pass
