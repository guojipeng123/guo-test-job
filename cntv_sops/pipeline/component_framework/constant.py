# -*- coding: utf-8 -*-
import copy

from pipeline.exceptions import ConstantNotExistException, ConstantReferenceException
from pipeline.core.data.expression import ConstantTemplate, deformat_constant_key
from pipeline.utils.graph import Graph


class ConstantPool(object):

    def __init__(self, pool, lazy=False):
        self.raw_pool = pool
        self.pool = None

        if not lazy:
            self.resolve()

    def resolve(self):
        if self.pool:
            return

        refs = self.get_reference_info()

        nodes = refs.keys()
        flows = []
        for node in nodes:
            for ref in refs[node]:
                if ref in nodes:
                    flows.append([node, ref])
        graph = Graph(nodes, flows)
        # circle reference check
        trace = graph.get_cycle()
        if trace:
            raise ConstantReferenceException('Exist circle reference between constants: %s' % '->'.join(trace))

        # resolve the constants reference
        pool = {}
        temp_pool = copy.deepcopy(self.raw_pool)
        # get those constants which are referenced only(not refer other constants)
        referenced_only = ConstantPool._get_referenced_only(temp_pool)
        while temp_pool:
            for ref in referenced_only:
                value = temp_pool[ref]['value']

                # resolve those constants which reference the 'ref'
                for key, info in temp_pool.items():
                    maps = {deformat_constant_key(ref): value}
                    temp_pool[key]['value'] = ConstantTemplate(info['value']).resolve_data(maps)

                pool[ref] = temp_pool[ref]
                temp_pool.pop(ref)
            referenced_only = ConstantPool._get_referenced_only(temp_pool)

        self.pool = pool

    @staticmethod
    def _get_referenced_only(pool):
        referenced_only = []
        for key, info in pool.items():
            reference = ConstantTemplate(info['value']).get_reference()
            formatted_reference = ['${%s}' % ref for ref in reference]
            reference = [c for c in formatted_reference if c in pool]
            if not reference:
                referenced_only.append(key)
        return referenced_only

    def get_reference_info(self, strict=True):
        refs = {}
        for key, info in self.raw_pool.items():
            reference = ConstantTemplate(info['value']).get_reference()
            formatted_reference = ['${%s}' % ref for ref in reference]
            ref = [c for c in formatted_reference if not strict or c in self.raw_pool]
            refs[key] = ref
        return refs

    def resolve_constant(self, constant):
        if not self.pool:
            self.resolve()

        if constant not in self.pool:
            raise ConstantNotExistException('constant %s not exist.' % constant)
        return self.pool[constant]['value']

    def resolve_value(self, val):
        if not self.pool:
            self.resolve()

        maps = {deformat_constant_key(key): self.pool[key]['value'] for key in self.pool}

        return ConstantTemplate(val).resolve_data(maps)
