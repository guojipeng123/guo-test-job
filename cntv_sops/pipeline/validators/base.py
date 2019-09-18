# -*- coding: utf-8 -*-


from pipeline import exceptions
from pipeline.validators.utils import validate_graph_connection, validate_graph_cycle, validate_converge_gateway


def validate_pipeline_tree(pipeline_tree, circle_free=False, strict_converge=True):
    check_connection = validate_graph_connection(pipeline_tree)
    if not check_connection['result']:
        raise exceptions.ParserWebTreeException(check_connection['message'])

    if not circle_free:
        check_cycle = validate_graph_cycle(pipeline_tree)
        if not check_cycle['result']:
            raise exceptions.ParserWebTreeException(check_cycle['message'])

    if strict_converge:
        validate_converge_gateway(pipeline_tree)
