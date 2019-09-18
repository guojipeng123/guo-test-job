# -*- coding: utf-8 -*-
from __future__ import absolute_import


def has_any_perms(user_obj, perms, obj):
    """
    @summary: if user_obj has any perm of perms, return True
    @param user_obj: instance of User
    @param perms: a list of perms
    @param obj: object
    @return: True or False
    """
    for perm in perms:
        if user_obj.has_perm(perm, obj):
            return True
    return False
