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
import json

__group_name__ = _(u"查看日志任务")  # 原子分类


class FindJobService(Service):  # 名字格式推荐：name+Service
    __need_schedule__ = False  # 异步轮巡

    def execute(self, data, parent_data):  # 执行函数，原子的执行逻辑，都放在这
        try:
            host = BK_PAAS_HOST
            api = '/api/c/compapi/v2/job/get_job_instance_log/'
            params = {
                "bk_app_code": APP_ID,
                'bk_app_secret': APP_TOKEN,
                'bk_username': data.get_one_of_inputs('bk_username', default=None),
                'bk_biz_id': data.get_one_of_inputs('bk_biz_id'),
                'job_instance_id': data.get_one_of_inputs('job_instance_id'),
            }
            result = requests.post(host + api, json=params).content
            print result
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
    name = _(u'找信息')
    code = 'find_job_test'
    bound_service = FindJobService
    form = settings.STATIC_URL + 'custom_atoms/test/find_job_test.js'
