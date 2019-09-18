# -*- coding: utf-8 -*-
from settings import APP_ID

# ===============================================================================
# 数据库设置, 本地环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': 'test-sops',  # 数据库名 (默认与APP_ID相同)
        'USER': 'root',  # 你的数据库user
        'PASSWORD': 'qwe123!@#',  # 你的数据库password
        'HOST': '127.0.0.1',  # 数据库HOST
        'PORT': 3306,  # 默认3306
    },
}

REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
}

# Import from local settings
try:
    from local_settings import *  # noqa
except ImportError:
    pass

LOG_PERSISTENT_DAYS = 1

# CELERY_ALWAYS_EAGER = True
# TEST_RUNNER = 'djcelery.contrib.test_runner.' \
#               'CeleryTestSuiteRunnerStoringResult'
