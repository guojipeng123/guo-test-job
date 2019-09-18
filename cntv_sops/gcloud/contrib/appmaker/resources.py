# -*- coding: utf-8 -*-
from django.http.response import HttpResponseForbidden
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest, ImmediateHttpResponse

from gcloud.conf import settings
from gcloud.tasktmpl3.resources import TaskTemplateResource
from gcloud.webservice3.resources import (
    get_business_for_user,
    GCloudModelResource,
    BusinessResource,
    AppSerializer,
    GCloudGenericAuthorization,
)
from gcloud.contrib.appmaker.models import AppMaker


class AppMakerResource(GCloudModelResource):
    business = fields.ForeignKey(
        BusinessResource,
        'business',
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
    template_scheme_id = fields.CharField(
        attribute='template_scheme_id',
        readonly=True,
        blank=True
    )
    task_template = fields.ForeignKey(
        TaskTemplateResource,
        'task_template',
    )
    template_id = fields.CharField(
        attribute='task_template_id',
        readonly=True,
        null=True
    )
    template_name = fields.CharField(
        attribute='task_template_name',
        readonly=True,
        null=True
    )
    category = fields.CharField(
        attribute='category',
        readonly=True,
        null=True
    )

    class Meta:
        queryset = AppMaker.objects.filter(is_deleted=False)
        resource_name = 'appmaker'
        excludes = []
        authorization = GCloudGenericAuthorization()
        always_return_data = True
        serializer = AppSerializer()
        filtering = {
            "business": ALL_WITH_RELATIONS,
            "template": ALL_WITH_RELATIONS,
            "name": ALL,
            "editor": ALL,
        }
        limit = 0

    def obj_delete(self, bundle, **kwargs):
        try:
            appmaker_id = kwargs['pk']
            appmaker = AppMaker.objects.get(pk=appmaker_id)
        except Exception:
            raise BadRequest('appmaker[id=%s] does not exist' % appmaker_id)
        biz_cc_id = appmaker.business.cc_id
        business = get_business_for_user(bundle.request.user, ['manage_business'])
        if not business.filter(cc_id=biz_cc_id).exists():
            raise ImmediateHttpResponse(HttpResponseForbidden('you have no permissions to delete appmaker'))

        if settings.RUN_MODE in ['PRODUCT', 'TEST']:
            fake = False
        else:
            fake = True
        result, data = AppMaker.objects.del_app_maker(
            biz_cc_id, appmaker_id, fake
        )
        if not result:
            raise BadRequest(data)
