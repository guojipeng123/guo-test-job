# -*- coding: utf-8 -*-
from django.conf.urls import url

from gcloud.contrib.function import views


urlpatterns = [
    url(r'^home/$', views.home),
]
