# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


# 任务流程创建方式
TASK_CREATE_METHOD = [
    ('app', _(u"手动")),
    ('api', _(u"API网关")),
    ('app_maker', _(u"轻应用")),
    ('periodic', _(u"周期任务")),
]

# 任务引用的流程模板来源
TEMPLATE_SOURCE = [
    ('business', _(u"业务流程")),
    ('common', _(u"公共流程")),
]
