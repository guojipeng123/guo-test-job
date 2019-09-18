# -*- coding: utf-8 -*-
from django.conf.urls import url

from gcloud.config import api

urlpatterns = [
    url(r'^api/biz_config/(?P<biz_cc_id>\d+)/$', api.biz_config),
    url(r'^api/biz_executor/(?P<biz_cc_id>\d+)/$', api.biz_executor),
]
