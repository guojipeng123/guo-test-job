# -*- coding: utf-8 -*-
"""
用于正式环境的全局配置
"""
import os


# ===============================================================================
# 数据库设置, 正式环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "cntv-sops",
        'USER': "root",
        'PASSWORD': "1qaz@WSX",
        'HOST': "10.77.65.49",
        'PORT': 3306,
    },
}

LOG_PERSISTENT_DAYS = 90
