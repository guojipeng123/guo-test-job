# -*- coding: utf-8 -*-
from jsonschema import Draft4Validator

from pipeline_web import exceptions
from pipeline_web.parser.schemas import WEB_PIPELINE_SCHEMA


def validate_web_pipeline_tree(web_pipeline_tree):
    valid = Draft4Validator(WEB_PIPELINE_SCHEMA)
    errors = []
    for error in sorted(valid.iter_errors(web_pipeline_tree), key=str):
        errors.append(u'%s: %s' % (u'→'.join(error.absolute_path), error.message))
    if errors:
        raise exceptions.ParserWebTreeException(','.join(errors))
