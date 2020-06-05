# -*- coding: utf-8 -*-
import base64
import hashlib
import itertools
import logging

import ujson as json
from django.db import transaction
from guardian.shortcuts import (
    assign_perm,
    remove_perm,
    get_users_with_perms,
    get_groups_with_perms,
)

from gcloud.conf import settings


logger = logging.getLogger("root")


@transaction.atomic
def assign_tmpl_perms(perms, groups, tmpl):
    # 先删除有当前要授权权限的分组权限
    perm_groups = get_groups_with_perms(tmpl, attach_perms=True)
    for group, perm_list in perm_groups.items():
        for perm in perm_list:
            if perm in perms:
                remove_perm(perm, group, tmpl)
    # 给分组授权
    for perm, group in itertools.product(perms, groups):
        assign_perm(perm, group, tmpl)


@transaction.atomic
def assign_tmpl_perms_user(perms, users, tmpl):
    # 先删除有当前要授权权限的用户权限
    perm_users = get_users_with_perms(tmpl, attach_perms=True)
    for user, perm_list in perm_users.items():
        for perm in perm_list:
            if perm in perms:
                remove_perm(perm, user, tmpl)
    # 给用户授权
    for perm, user in itertools.product(perms, users):
        assign_perm(perm, user, tmpl)


def read_template_data_file(f):
    if not f:
        return {
            'result': False,
            'message': 'Upload template dat file please.'
        }

    content = f.read()
    try:
        file_data = json.loads(base64.b64decode(content))
    except Exception:
        return {
            'result': False,
            'message': 'File is corrupt'
        }

    # check the validation of file
    templates_data = file_data['template_data']
    digest = hashlib.md5(json.dumps(templates_data, sort_keys=True) + settings.TEMPLATE_DATA_SALT).hexdigest()

    is_data_valid = (digest == file_data['digest'])
    if not is_data_valid:
        return {
            'result': False,
            'message': 'Invalid template data'
        }

    return {
        'result': True,
        'data': file_data
    }