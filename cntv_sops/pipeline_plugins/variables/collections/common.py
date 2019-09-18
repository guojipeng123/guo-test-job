# -*- coding: utf-8 -*-
import logging

from pipeline.conf import settings
from pipeline.core.data.var import LazyVariable

logger = logging.getLogger('root')


class Password(LazyVariable):
    code = 'password'
    form = '%svariables/password.js' % settings.STATIC_URL

    def get_value(self):
        return self.value


class Select(LazyVariable):
    code = 'select'
    meta_form = '%svariables/select_meta.js' % settings.STATIC_URL
    form = '%svariables/select.js' % settings.STATIC_URL

    def get_value(self):
        if isinstance(self.value, dict):
            if self.value['type'] == '1':
                return self.value['default'].split(',')
            else:
                return self.value['default']
        return self.value
