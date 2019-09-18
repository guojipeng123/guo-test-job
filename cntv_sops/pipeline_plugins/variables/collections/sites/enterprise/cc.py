# -*- coding: utf-8 -*-
import logging

from pipeline.conf import settings
from pipeline_plugins.components.utils import (
    cc_get_ips_info_by_str
)
from pipeline.core.data.var import LazyVariable
from pipeline_plugins.components.utils import get_ip_by_regex

logger = logging.getLogger('root')


class VarIpPickerVariable(LazyVariable):
    code = 'var_ip_picker'
    form = '%svariables/sites/%s/var_ip_picker.js' % (settings.STATIC_URL, settings.RUN_VER)

    def get_value(self):
        var_ip_picker = self.value
        username = self.pipeline_data['executor']
        biz_cc_id = self.pipeline_data['biz_cc_id']

        produce_method = var_ip_picker['var_ip_method']
        if produce_method == 'custom':
            custom_value = var_ip_picker['var_ip_custom_value']
            data = cc_get_ips_info_by_str(username, biz_cc_id, custom_value)
            ip_list = data['ip_result']
            data = ','.join([ip['InnerIP'] for ip in ip_list])
        else:
            select_data = var_ip_picker['var_ip_tree']
            select_ip = map(lambda x: get_ip_by_regex(x)[0], filter(lambda x: get_ip_by_regex(x), select_data))
            data = ','.join(list(set(select_ip)))

        return data
