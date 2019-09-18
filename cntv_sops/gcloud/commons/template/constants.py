# -*- coding: utf-8 -*-


# template and taskflow permission names
class PermName(object):
    CREATE_TASK_PERM_NAME = 'create_task'
    FILL_PARAMS_PERM_NAME = 'fill_params'
    EXECUTE_TASK_PERM_NAME = 'execute_task'
    PERM_LIST = [CREATE_TASK_PERM_NAME,
                 FILL_PARAMS_PERM_NAME,
                 EXECUTE_TASK_PERM_NAME]


PermNm = PermName()
