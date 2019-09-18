# -*- coding: utf-8 -*-
from pipeline.parser.pipeline_parser import PipelineParser

from pipeline_web.parser.format import format_web_data_to_pipeline
from pipeline_web.parser.validator import validate_web_pipeline_tree


class WebPipelineAdapter(PipelineParser):

    def __init__(self, web_pipeline_tree):
        validate_web_pipeline_tree(web_pipeline_tree)
        pipeline_tree = format_web_data_to_pipeline(web_pipeline_tree)
        super(WebPipelineAdapter, self).__init__(pipeline_tree)
