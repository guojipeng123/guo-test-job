# -*- coding: utf-8 -*-
from django.conf.urls import url
from gcloud.contrib.analysis import views

urlpatterns = [
    url(r'^query_instance_by_group/$', views.query_instance_by_group),
    url(r'^query_template_by_group/$', views.query_template_by_group),
    url(r'^query_atom_by_group/$', views.query_atom_by_group),
    url(r'^query_appmaker_by_group/$', views.query_appmaker_by_group),
    url(r'^template/$', views.analysis_home),
    url(r'^instance/$', views.analysis_home),
    url(r'^appmaker/$', views.analysis_home),
    url(r'^atom/$', views.analysis_home),
    url(r'^get_task_category/$', views.get_task_category),
]
