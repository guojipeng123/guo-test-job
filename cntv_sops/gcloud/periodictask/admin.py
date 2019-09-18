# -*- coding: utf-8 -*-

from django.contrib import admin

from gcloud.periodictask import models


@admin.register(models.PeriodicTask)
class PeriodicTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'total_run_count', 'last_run_at', 'creator', 'business', 'template_id']
    search_fields = ['id']


@admin.register(models.PeriodicTaskHistory)
class PeriodicTaskHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_at', 'ex_data', 'start_success', 'task']
    search_fields = ['task__id']
