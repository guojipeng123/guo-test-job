# -*- coding: utf-8 -*-


class VariableLibrary(object):
    variables = {}

    @classmethod
    def get_var_class(cls, code):
        return cls.variables.get(code)

    @classmethod
    def get_var(cls, code, name, data, context=None, pipeline_data=None):
        if not context:
            return cls.variables[code](name, data)
        return cls.variables[code](name, data, context, pipeline_data)
