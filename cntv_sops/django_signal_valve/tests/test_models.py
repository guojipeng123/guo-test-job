# -*- coding: utf-8 -*-
from django.test import TestCase

from django_signal_valve.models import Signal


class TestModels(TestCase):

    def tearDown(self):
        Signal.objects.all().delete()

    def test_manager_dump(self):
        kwargs = {'key1': 'value1',
                  'key2': [1, 2, 3],
                  'key3': {'key4': 'value4'}}
        Signal.objects.dump(module_path='path', signal_name='name', kwargs=kwargs)
        signal = Signal.objects.all()[0]
        self.assertEqual(signal.module_path, 'path')
        self.assertEqual(signal.name, 'name')
        self.assertEqual(signal.kwargs, kwargs)
