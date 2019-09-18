# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import query


urlpatterns = [
    url(r'^cc_search_object_attribute/(?P<obj_id>\w+)/(?P<biz_cc_id>\d+)/$',
        query.cc_search_object_attribute),
    url(r'^cc_search_create_object_attribute/(?P<obj_id>\w+)/(?P<biz_cc_id>\d+)/$',
        query.cc_search_create_object_attribute),
    url(r'^cc_search_topo/(?P<obj_id>\w+)/(?P<category>\w+)/(?P<biz_cc_id>\d+)/$', query.cc_search_topo),
    url(r'^cc_get_host_by_module_id/(?P<biz_cc_id>\d+)/$', query.cc_get_host_by_module_id),
    url(r'^job_get_script_list/(?P<biz_cc_id>\d+)/$', query.job_get_script_list),
]
