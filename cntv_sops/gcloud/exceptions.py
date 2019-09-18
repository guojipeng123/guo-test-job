# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


class Unauthorized(Exception):
    pass


class Forbidden(Exception):
    pass


class NotFound(Exception):
    pass


class APIError(Exception):

    def __init__(self, system, api, message):
        self.system = system
        self.api = api
        self.message = message

    @property
    def error(self):
        return u'%s【%s】%s【%s】%s【%s】%s' % (
            _(u'请求第三方系统'),
            self.system,
            _(u'接口'),
            self.api,
            _(u'异常'),
            self.message,
            _(u'请联系第三方系统负责人处理'))


class BadTaskOperation(Exception):
    pass


class BadResourceClass(Exception):
    pass


class FlowExportError(Exception):
    pass
