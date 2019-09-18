# -*- coding:utf-8 -*-

from django.contrib import admin

from django_signal_valve.models import Signal


@admin.register(Signal)
class SignalAdmin(admin.ModelAdmin):
    list_display = ['id', 'module_path', 'name', 'kwargs']
    search_fields = ['id', 'module_path', 'name']
