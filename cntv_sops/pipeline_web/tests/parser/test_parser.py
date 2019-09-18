# -*- coding: utf-8 -*-
import unittest

from pipeline.core.pipeline import Pipeline

from pipeline_web.parser import WebPipelineAdapter
from .data import (
    WEB_PIPELINE_DATA,
    WEB_PIPELINE_WITH_SUB_PROCESS,
    WEB_PIPELINE_WITH_SUB_PROCESS2,
    id_list2
)


class TestPipelineParser(unittest.TestCase):

    def setUp(self):
        from pipeline.component_framework.component import Component
        from pipeline.core.flow.activity import Service

        class TestService(Service):
            def execute(self, data, parent_data):
                return True

            def outputs_format(self):
                return []

        class TestComponent(Component):
            name = 'test'
            code = 'test'
            bound_service = TestService
            form = 'test.js'

    def test_web_pipeline_parser(self):
        parser_obj = WebPipelineAdapter(WEB_PIPELINE_DATA)
        self.assertIsInstance(parser_obj.parse(), Pipeline)

    def test_web_pipeline_parser_subprocess(self):
        parser_obj = WebPipelineAdapter(WEB_PIPELINE_WITH_SUB_PROCESS)
        self.assertIsInstance(parser_obj.parse(), Pipeline)

    def test_web_pipeline_parser2(self):
        parser_obj = WebPipelineAdapter(WEB_PIPELINE_WITH_SUB_PROCESS2)
        self.assertIsInstance(parser_obj.parse(), Pipeline)

    def test_pipeline_get_act_inputs(self):
        parser_obj = WebPipelineAdapter(WEB_PIPELINE_WITH_SUB_PROCESS2)
        act_inputs = parser_obj.get_act_inputs(id_list2[3], [id_list2[10]])
        self.assertEqual(
            act_inputs,
            {
                'input_test': 'custom2',
                'radio_test': '1',
            }
        )
