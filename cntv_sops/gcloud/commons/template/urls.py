# -*- coding: utf-8 -*-
from django.conf.urls import url

from gcloud.commons.template import api


urlpatterns = [
    url(r'^api/form/$', api.form),
    url(r'^api/get_perms/$', api.get_perms),
    url(r'^api/save_perms/$', api.save_perms),
    url(r'^api/export/$', api.export_templates),
    url(r'^api/import/$', api.import_templates),
    url(r'^api/import_check/$', api.check_before_import),
]
