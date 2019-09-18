# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from settings import BK_PAAS_HOST, APP_CODE
from blueking.component.shortcuts import (get_client_by_request,
                                          ComponentClient,
                                          get_client_by_user)

ESB_GET_CLIENT_BY_REQUEST = get_client_by_request
ESB_GET_CLIENT_BY_USER = get_client_by_user
ESB_COMPONENT_CLIENT = ComponentClient

ESB_AUTH_COMPONENT_SYSTEM = 'bk_login'
ESB_AUTH_GET_USER_INFO = 'get_user'

# 针对CC接口数据相关的缓存时间(单位s)
DEFAULT_CACHE_TIME_FOR_CC = 5

# 针对本地用户信息更新标志缓存的时间
DEFAULT_CACHE_TIME_FOR_USER_UPDATE = 5

# 针对平台用户接口缓存的时间
DEFAULT_CACHE_TIME_FOR_AUTH = 5

REMOTE_ANALYSIS_URL = '%s/console/static/js/analysis.min.js' % BK_PAAS_HOST
REMOTE_API_URL = '%s/console/static/bk_api/api.js' % BK_PAAS_HOST

RUN_VER_NAME = _(u"蓝鲸智云企业版")

APP_HOST = '%s/o/%s/' % (BK_PAAS_HOST, APP_CODE)
TEST_APP_HOST = '%s/t/%s/' % (BK_PAAS_HOST, APP_CODE)

APP_MAKER_LINK_PREFIX = '%sappmaker/' % APP_HOST
TEST_APP_MAKER_LINK_PREFIX = '%sappmaker/' % TEST_APP_HOST
APP_MAKER_UPLOAD_LOGO_URL = '%s/paas/api/app_maker/app_logo/modify/' % BK_PAAS_HOST
APP_MAKER_UPLOAD_LOGO_USER_UIN = 'bk_token'
APP_MAKER_UPLOAD_LOGO_USER_KEY = 'bk_token_null'

IMPORT_V1_TEMPLATE_FLAG = False

RSA_PUB_KEY = "-----BEGIN PUBLIC KEY-----\\n" + \
              "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCr5dIZVAp6ia+tLVlDKPUZP4RD\\n" + \
              "7sH+Rbc9eHIy46OoBQeLgRhp93MEarByPlSdO0BveWi/o7PzAxTX3aev2PobfuDk\\n" + \
              "CG0xQNpyXtq7NMU9GP4lo9MDeEw0+GNvzKjxl4sn9ajCvAFMRcAt61/JqIQnxE+/\\n" + \
              "iymoAVK67gfTOTvckQIDAQAB\\n" + \
              "-----END PUBLIC KEY-----"
