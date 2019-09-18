# -*- coding: utf-8 -*-
from django.conf.urls import url

from gcloud.periodictask import api

urlpatterns = [
    url(r'^api/enabled/(?P<biz_cc_id>\d+)/(?P<task_id>\d+)/$', api.set_enabled_for_periodic_task),
    url(r'^api/cron/(?P<biz_cc_id>\d+)/(?P<task_id>\d+)/$', api.modify_cron),
    url(r'^api/constants/(?P<biz_cc_id>\d+)/(?P<task_id>\d+)/$', api.modify_constants)
]
