# -*- coding: utf-8 -*-
import json
import logging

import pytz
from django.http import HttpResponse, HttpResponseForbidden
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from gcloud import exceptions
from gcloud.core.utils import prepare_business


logger = logging.getLogger("root")


class GCloudPermissionMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        If a request path contains biz_cc_id parameter, check if current
        user has perm view_business or return http 403.
        """
        if getattr(view_func, 'login_exempt', False):
            return None
        biz_cc_id = view_kwargs.get('biz_cc_id')
        if biz_cc_id and str(biz_cc_id) != '0':
            try:
                business = prepare_business(request, cc_id=biz_cc_id)
            except exceptions.Unauthorized:
                # permission denied for target business (irregular request)
                return HttpResponse(status=401)
            except exceptions.Forbidden:
                # target business does not exist (irregular request)
                return HttpResponseForbidden()
            except exceptions.APIError as e:
                ctx = {
                    'system': e.system,
                    'api': e.api,
                    'message': e.message,
                }
                logger.error(json.dumps(ctx))
                return HttpResponse(status=503, content=json.dumps(ctx))

            # set time_zone of business
            if business.time_zone:
                request.session['blueking_timezone'] = business.time_zone

            if not request.user.has_perm('view_business', business):
                return HttpResponseForbidden()


class UnauthorizedMiddleware(object):

    def process_response(self, request, response):
        # 403: PaaS 平台用来控制应用白名单和 IP 白名单
        # 405: 用户无当前业务或者数据的查询/操作权限
        if response.status_code in (403,):
            response = HttpResponse(
                content=_(u"您没有权限进行此操作"),
                status=405
            )
        return response


class TimezoneMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        tzname = request.session.get('blueking_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
