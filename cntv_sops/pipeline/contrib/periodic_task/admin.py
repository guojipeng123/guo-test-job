# -*- coding: utf-8 -*-

from django.contrib import admin

from pipeline.contrib.periodic_task import models


@admin.register(models.PeriodicTask)
class PeriodicTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'total_run_count', 'last_run_at', 'creator']
    search_fields = ['id', 'name']


@admin.register(models.PeriodicTaskHistory)
class PeriodicTaskHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_at', 'ex_data', 'start_success', 'periodic_task']
    search_fields = ['periodic_task__id']


@admin.register(models.CrontabSchedule)
class CrontabScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year', 'timezone']


@admin.register(models.DjCeleryPeriodicTask)
class DjCeleryPeriodicTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'task', 'enabled', 'queue', 'last_run_at', 'total_run_count', 'crontab']
    search_fields = ['id', 'name', 'task', 'enabled']
