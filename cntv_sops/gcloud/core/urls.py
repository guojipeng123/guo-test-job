# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.i18n import javascript_catalog

from gcloud.core import views, api, command


urlpatterns = [
    url(r'^$', views.home),
    url(r'^business/home/(?P<biz_cc_id>\d+)/$', views.biz_home),
    url(r'^set_lang/$', views.set_language),

    url(r'^core/api/get_basic_info/$', api.get_basic_info),
    url(r'^core/api/change_default_business/(?P<biz_cc_id>\d+)/$', api.change_default_business),
    url(r'^core/api/get_roles_and_personnel/(?P<biz_cc_id>\d+)/$', api.get_roles_and_personnel),

    url(r'^core/get_cache_key/(?P<key>\w+)/$', command.get_cache_key),
    url(r'^core/delete_cache_key/(?P<key>\w+)/$', command.delete_cache_key),

    # i18n
    url(r'^jsi18n/(?P<packages>\S+?)/$', javascript_catalog)
]
