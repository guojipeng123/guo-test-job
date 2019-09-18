# -*- coding:utf-8 -*-
__author__ = 'foxnick'
# @Time    : 2019/8/11 8:00
# @Email   : foxnick@canway.net
from django.utils.translation import ugettext_lazy as _
from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component
from common.log import logger
import requests, os
from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST

__group_name__ = _(u"测试")  # 原子分类


class BKAPIService(Service):  # 名字格式推荐：name+Service
    __need_schedule__ = False  # 异步轮巡

    def execute(self, data, parent_data):  # 执行函数，原子的执行逻辑，都放在这
        try:
            host = os.environ.get('BK_PAAS_HOST', BK_PAAS_HOST)
            api = data.get_one_of_inputs('api')
            params = {
                "bk_app_code": os.environ.get('APP_ID', APP_ID),
                'bk_app_secret': os.environ.get('APP_TOKEN', APP_TOKEN),
                'bk_username': data.get_one_of_inputs('bk_username', default=None)
            }
            extra_dict = eval(data.get_one_of_inputs('extra_dict', default='{}'))
            params = dict(params, **extra_dict)
            result = requests.post(host+api, json=params).content
            data.set_outputs('result', result)  # data.set_outputs()方法是将key和value，设置到缓存队列里
            return True
        except Exception, e:
            logger.exception("execute")
            data.set_outputs('error_msg', str(e))  # 将异常信息输出到前端
            data.set_outputs('error_state', "false")
            return False

    def schedule(self, data, parent_data, callback_data=None):  # 轮巡函数

        return True

    def outputs_format(self):  # 输出结果
        return [
            self.OutputItem(name=_(u'执行结果'), key='result', type='str'),
            self.OutputItem(name=_(u'异常信息'), key='error_msg', type='str'),
            self.OutputItem(name=_(u'异常状态码'), key='error_state', type='str'),
        ]


class BKAPIComponent(Component):
    name = _(u'蓝鲸api')
    code = 'bk_api_test'
    bound_service = BKAPIService
    form = settings.STATIC_URL + 'custom_atoms/test/bk_api_test.js'
