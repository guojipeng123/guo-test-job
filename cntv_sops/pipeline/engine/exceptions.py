# -*- coding: utf-8 -*-
from pipeline.exceptions import PipelineException


class PipelineEngineException(PipelineException):
    pass


class NodeNotExistException(PipelineEngineException):
    pass


class InvalidOperationException(PipelineEngineException):
    pass


class RabbitMQConnectionError(PipelineEngineException):
    pass


class ChildDataSyncError(PipelineEngineException):
    pass


class DataRetrieveError(PipelineEngineException):
    pass


class InvalidDataBackendError(PipelineEngineException):
    pass
