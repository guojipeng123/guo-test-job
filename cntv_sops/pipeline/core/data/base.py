# -*- coding: utf-8 -*-
try:
    import ujson as json
except ImportError:
    import json
import copy

from pipeline import exceptions
from pipeline.utils.collections import FancyDict


class DataObject(object):
    def __init__(self, inputs, outputs=None):
        if not isinstance(inputs, dict):
            raise exceptions.DataTypeErrorException('inputs is not dict')
        self.inputs = FancyDict(inputs)
        if outputs is None:
            outputs = {}
        if not isinstance(outputs, dict):
            raise exceptions.DataTypeErrorException('outputs is not dict')
        self.outputs = FancyDict(outputs)

    def get_inputs(self):
        return self.inputs

    def get_outputs(self):
        return self.outputs

    def get_one_of_inputs(self, key, default=None):
        return self.inputs.get(key, default)

    def get_one_of_outputs(self, key, default=None):
        return self.outputs.get(key, default)

    def set_outputs(self, key, value):
        self.outputs.update({key: value})
        return True

    def reset_outputs(self, outputs):
        if not isinstance(outputs, dict):
            raise exceptions.DataTypeErrorException('outputs is not dict')
        self.outputs = FancyDict(outputs)
        return True

    def update_outputs(self, dic):
        self.outputs.update(dic)

    def inputs_copy(self):
        return copy.copy(self.inputs)

    def outputs_copy(self):
        return copy.copy(self.outputs)

    def override_inputs(self, inputs):
        if not isinstance(inputs, FancyDict):
            inputs = FancyDict(inputs)
        self.inputs = inputs

    def override_outputs(self, outputs):
        if not isinstance(outputs, FancyDict):
            outputs = FancyDict(outputs)
        self.outputs = outputs

    def serializer(self):
        result = {
            'inputs': self.inputs,
            'outputs': self.outputs
        }
        return json.dumps(result)
