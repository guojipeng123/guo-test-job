# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from conf.urls_custom import urlpatterns_custom
from gcloud.core.views import page_not_found

urlpatterns = [
    # django后台数据库管理
    url(r'^admin/', include(admin.site.urls)),
    # 用户账号--不要修改
    url(r'^accounts/', include('account.urls')),
]

# app自定义路径
urlpatterns += urlpatterns_custom

if settings.RUN_MODE == 'DEVELOP':
    urlpatterns += [
        # media
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
            ),
    ]
    if not settings.DEBUG:
        urlpatterns += [
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}
                ),
        ]

handler404 = page_not_found
