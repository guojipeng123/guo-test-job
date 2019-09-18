# -*- coding: utf-8 -*-

from django.conf.urls import url

from gcloud.contrib.appmaker import views, api

urlpatterns = [
    # 新建、编辑轻应用
    url(r'^save/(?P<biz_cc_id>\d+)/$', api.save),

    # mini-app 内链接

    # 打开一个轻应用，直接进入参数填写阶段
    url(r'^(?P<app_id>\d+)/newtask/(?P<biz_cc_id>\d+)/selectnode/$', views.newtask_selectnode),
    url(r'^(?P<app_id>\d+)/newtask/(?P<biz_cc_id>\d+)/paramfill/$', views.newtask_paramfill),
    # 从轻应用的任务记录跳转到任务详情
    url(r'^(?P<app_id>\d+)/execute/(?P<biz_cc_id>\d+)/$', views.execute),
    # 轻应用中任务列表
    url(r'^(?P<app_id>\d+)/task_home/(?P<biz_cc_id>\d+)/$', views.task_home),
    url(r'^get_appmaker_count/(?P<biz_cc_id>\d+)/$', api.get_appmaker_count),
]
