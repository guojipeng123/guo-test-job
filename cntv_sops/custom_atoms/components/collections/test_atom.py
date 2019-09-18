# -*- coding:utf-8 -*-
__author__ = 'foxnick'
# @Time    : 2019/8/11 8:00
# @Email   : foxnick@canway.net
from django.utils.translation import ugettext_lazy as _
from pipeline.conf import settings
from pipeline.core.flow.activity import Service
from pipeline.component_framework.component import Component
from common.log import logger

__group_name__ = _(u"测试")  # 原子分类


class TestService(Service):  # 名字格式推荐：name+Service
    __need_schedule__ = False  # 异步轮巡

    def execute(self, data, parent_data):  # 执行函数，原子的执行逻辑，都放在这
        try:
            value1 = int(data.get_one_of_inputs("cntv_value1"))
            value2 = int(data.get_one_of_inputs("cntv_value2"))
            symbol = data.get_one_of_inputs("symbol")
            if symbol == "+":
                result = value1 + value2
            elif symbol == "-":
                result = value1 * value2
            elif symbol == "*":
                result = value1 * value2
            elif symbol == "/":
                result = value1 / value2
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


class Testomponent(Component):
    name = _(u'我是测试一个原子')
    code = 'cn_test'
    bound_service = TestService
    form = settings.STATIC_URL + 'custom_atoms/test/cntv_test.js'
