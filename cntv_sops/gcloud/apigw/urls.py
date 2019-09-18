# -*- coding: utf-8 -*-
from django.conf.urls import url

from gcloud.apigw import views

urlpatterns = [
    url(r'^get_template_list/(?P<bk_biz_id>\d+)/$', views.get_template_list),
    url(r'^get_template_info/(?P<template_id>\d+)/(?P<bk_biz_id>\d+)/$', views.get_template_info),
    url(r'^create_task/(?P<template_id>\d+)/(?P<bk_biz_id>\d+)/$', views.create_task),
    url(r'^start_task/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.start_task),
    url(r'^operate_task/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.operate_task),
    url(r'^get_task_status/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.get_task_status),
    url(r'^query_task_count/(?P<bk_biz_id>\d+)/$', views.query_task_count),
    url(r'^get_periodic_task_list/(?P<bk_biz_id>\d+)/$', views.get_periodic_task_list),
    url(r'^get_periodic_task_info/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.get_periodic_task_info),
    url(r'^create_periodic_task/(?P<template_id>\d+)/(?P<bk_biz_id>\d+)/$', views.create_periodic_task),
    url(r'^set_periodic_task_enabled/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.set_periodic_task_enabled),
    url(r'^modify_cron_for_periodic_task/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.modify_cron_for_periodic_task),
    url(r'^modify_constants_for_periodic_task/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$',
        views.modify_constants_for_periodic_task),
    url(r'^get_task_detail/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.get_task_detail),
    url(r'^get_task_node_detail/(?P<task_id>\d+)/(?P<bk_biz_id>\d+)/$', views.get_task_node_detail),
]
