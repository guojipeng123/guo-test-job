# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ComponentInTemplate, ComponentExecuteData, TemplateInPipeline, InstanceInPipeline


@admin.register(ComponentInTemplate)
class ComponentInTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'component_code',
        'template_id',
        'node_id',
        'is_sub',
    )
    search_fields = (
        'template_id',
        'node_id',
    )
    list_filter = ('component_code', 'is_sub')


@admin.register(ComponentExecuteData)
class ComponentExecuteDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'component_code',
        'instance_id',
        'node_id',
        'is_sub',
        'started_time',
        'archived_time',
        'elapsed_time',
        'status',
        'is_skip',
        'is_retry'
    )
    search_fields = (
        'instance_id',
        'node_id',
    )
    list_filter = (
        'component_code',
        'is_sub',
        'status',
        'is_skip',
    )


@admin.register(TemplateInPipeline)
class TemplateInPipelineAdmin(admin.ModelAdmin):
    list_display = (
        'template_id',
        'atom_total',
        'subprocess_total',
        'gateways_total'
    )

    search_fields = (
        'template_id'
    )
    list_filter = (
        'template_id',
        'atom_total',
        'subprocess_total',
        'gateways_total'
    )


@admin.register(InstanceInPipeline)
class InstanceInPipelineAdmin(admin.ModelAdmin):
    list_display = (
        'instance_id',
        'atom_total',
        'subprocess_total',
        'gateways_total'
    )

    search_fields = (
        'instance_id'
    )
    list_filter = (
        'instance_id',
        'atom_total',
        'subprocess_total',
        'gateways_total'
    )
