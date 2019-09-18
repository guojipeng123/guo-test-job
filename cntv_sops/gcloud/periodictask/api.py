# -*- coding: utf-8 -*-

from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST

from gcloud.utils.forms import post_form_validator
from gcloud.core.models import Business
from gcloud.periodictask.models import PeriodicTask
from gcloud.core.decorators import check_user_perm_of_business
from gcloud.taskflow3.forms import (PeriodicTaskCronModifyForm,
                                    PeriodicTaskEnabledSetForm,
                                    PeriodicTaskConstantsModifyForm)


@require_POST
@check_user_perm_of_business('manage_business')
@post_form_validator(PeriodicTaskEnabledSetForm)
def set_enabled_for_periodic_task(request, biz_cc_id, task_id):
    enabled = request.form.clean()['enabled']

    try:
        task = PeriodicTask.objects.get(id=task_id, business__cc_id=biz_cc_id)
    except PeriodicTask.DoesNotExist:
        return HttpResponseForbidden()

    task.set_enabled(enabled)

    return JsonResponse({
        'result': True,
        'message': 'success'
    })


@require_POST
@check_user_perm_of_business('manage_business')
@post_form_validator(PeriodicTaskCronModifyForm)
def modify_cron(request, biz_cc_id, task_id):
    cron = request.form.clean()['cron']

    try:
        tz = Business.objects.get(cc_id=biz_cc_id).time_zone
        task = PeriodicTask.objects.get(id=task_id, business__cc_id=biz_cc_id)
    except PeriodicTask.DoesNotExist:
        return HttpResponseForbidden()

    try:
        task.modify_cron(cron, tz)
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': e.message
        })

    return JsonResponse({
        'result': True,
        'message': 'success'
    })


@require_POST
@check_user_perm_of_business('manage_business')
@post_form_validator(PeriodicTaskConstantsModifyForm)
def modify_constants(request, biz_cc_id, task_id):
    constants = request.form.clean()['constants']

    try:
        task = PeriodicTask.objects.get(id=task_id, business__cc_id=biz_cc_id)
    except PeriodicTask.DoesNotExist:
        return HttpResponseForbidden()

    try:
        new_constants = task.modify_constants(constants)
    except Exception as e:
        return JsonResponse({
            'result': False,
            'message': e.message
        })

    return JsonResponse({
        'result': True,
        'message': 'success',
        'data': new_constants
    })
