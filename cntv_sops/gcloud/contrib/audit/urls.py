# -*- coding: utf-8 -*-
from django.conf.urls import url

from gcloud.contrib.audit import views


urlpatterns = [
    url(r'^home/$', views.home),
]
