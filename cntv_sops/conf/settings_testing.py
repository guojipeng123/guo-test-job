# -*- coding: utf-8 -*-
"""
用于测试环境的全局配置
"""
from settings import APP_ID

# ===============================================================================
# 数据库设置, 测试环境数据库设置
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


LOG_PERSISTENT_DAYS = 30
