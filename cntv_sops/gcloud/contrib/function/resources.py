# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from bk_api import is_user_functor

from gcloud.webservice3.resources import (
    GCloudModelResource,
    AppSerializer,
)
from gcloud.taskflow3.resources import TaskFlowInstanceResource
from gcloud.contrib.function.models import FunctionTask


class FunctionTaskResource(GCloudModelResource):
    task = fields.ForeignKey(
        TaskFlowInstanceResource,
        'task',
        full=True
    )
    creator_name = fields.CharField(
        attribute='creator_name',
        readonly=True,
        null=True
    )
    editor_name = fields.CharField(
        attribute='editor_name',
        readonly=True,
        null=True
    )
    status_name = fields.CharField(
        attribute='status_name',
        readonly=True,
        null=True
    )

    class Meta:
        queryset = FunctionTask.objects.all()
        resource_name = 'function_task'
        excludes = []
        q_fields = ['task__pipeline_instance__name']
        authorization = ReadOnlyAuthorization()
        always_return_data = True
        serializer = AppSerializer()
        filtering = {
            "task": ALL_WITH_RELATIONS,
            "creator": ALL,
            "editor": ALL,
            "status": ALL,
        }
        limit = 0

    def get_object_list(self, request):
        if is_user_functor(request) or request.user.is_superuser:
            return super(FunctionTaskResource, self).get_object_list(request)
        else:
            return super(FunctionTaskResource, self).get_object_list(request).none()
