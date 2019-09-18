# -*- coding: utf-8 -*-
from django.conf.urls import url

from gcloud.taskflow3 import views, api

urlpatterns = [
    url(r'^home/(?P<biz_cc_id>\d+)/$', views.home),
    url(r'^api/status/(?P<biz_cc_id>\d+)/$', api.status),
    url(r'^api/clone/(?P<biz_cc_id>\d+)/$', api.task_clone),
    url(r'^api/action/(?P<action>\w+)/(?P<biz_cc_id>\d+)/$', api.task_action),

    url(r'^api/flow/claim/(?P<biz_cc_id>\d+)/$', api.task_func_claim),
    url(r'^api/inputs/modify/(?P<biz_cc_id>\d+)/$', api.task_modify_inputs),
    url(r'^api/nodes/action/(?P<action>\w+)/(?P<biz_cc_id>\d+)/$', api.nodes_action),
    url(r'^api/nodes/data/(?P<biz_cc_id>\d+)/$', api.data),
    url(r'^api/nodes/detail/(?P<biz_cc_id>\d+)/$', api.detail),
    url(r'^api/nodes/get_job_instance_log/(?P<biz_cc_id>\d+)/$', api.get_job_instance_log),
    url(r'^api/nodes/spec/timer/reset/(?P<biz_cc_id>\d+)/$', api.spec_nodes_timer_reset),

    url(r'^api/preview_task_tree/(?P<biz_cc_id>\d+)/$', api.preview_task_tree),
    url(r'^api/query_task_count/(?P<biz_cc_id>\d+)/$', api.query_task_count),
    url(r'^api/nodes/log/(?P<biz_cc_id>\d+)/(?P<node_id>\w+)/$', api.get_node_log),
    url(r'^api/get_task_create_method/$', api.get_task_create_method)

]
