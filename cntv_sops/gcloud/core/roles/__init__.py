# -*- coding: utf-8 -*-
import importlib

from django.conf import settings

roles = importlib.import_module('gcloud.core.roles.sites.%s.roles' % settings.RUN_VER)

export_var = ['ROLES_DECS',
              'ALL_ROLES',
              'ADMIN_ROLES',
              'CC_ROLES',
              'CC_PERSON_GROUP',
              'DEFAULT_CC_NOTIFY_SET',
              'MAINTAINERS',
              'PRODUCTPM',
              'DEVELOPER',
              'TESTER',
              'OWNER',
              'COOPERATION',
              'ADMIN',
              'FUNCTOR',
              'AUDITOR']

for role_var in export_var:
    locals()[role_var] = getattr(roles, role_var)

__all__ = export_var
