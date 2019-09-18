# -*- coding: utf-8 -*-
import importlib

from django.conf.urls import url
from django.conf import settings

from gcloud.tasktmpl3 import api

import_data = importlib.import_module('gcloud.tasktmpl3.sites.%s.import_data' % settings.RUN_VER)
import_v2_data = importlib.import_module('gcloud.tasktmpl3.sites.%s.import_data_2_to_3' % settings.RUN_VER)

urlpatterns = [
    url(r'^api/form/(?P<biz_cc_id>\d+)/$', api.form),
    url(r'^api/collect/(?P<biz_cc_id>\d+)/$', api.collect),
    url(r'^api/get_perms/(?P<biz_cc_id>\d+)/$', api.get_perms),
    url(r'^api/save_perms/(?P<biz_cc_id>\d+)/$', api.save_perms),
    url(r'^get_business_basic_info/(?P<biz_cc_id>\d+)/$', api.get_business_basic_info),

    url(r'^api/import_v1/(?P<biz_cc_id>\d+)/$', import_data.import_v1),
    url(r'^api/import_v2/$', import_v2_data.import_v2),
    url(r'^api/export/(?P<biz_cc_id>\d+)/$', api.export_templates),
    url(r'^api/import/(?P<biz_cc_id>\d+)/$', api.import_templates),
    url(r'^api/import_check/(?P<biz_cc_id>\d+)/$', api.check_before_import),
    url(r'^api/replace_node_id/$', api.replace_all_templates_tree_node_id),
    url(r'^api/import_and_replace_job_id/(?P<biz_cc_id>\d+)/$', api.import_preset_template_and_replace_job_id),
    url(r'^api/get_template_count/(?P<biz_cc_id>\d+)/$', api.get_template_count),
    url(r'^api/get_collect_template/(?P<biz_cc_id>\d+)/$', api.get_collect_template),
]
