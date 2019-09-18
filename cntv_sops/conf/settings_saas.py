# -*- coding: utf-8 -*-
"""
SaaS上传部署的全局配置
"""
import os
from .default import APP_ID

# ===============================================================================
# 数据库设置, 正式环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', APP_ID),
        'USER': os.environ.get('DB_USERNAME', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '123456'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    },
}
