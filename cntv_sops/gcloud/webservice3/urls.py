# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from tastypie.api import Api

from gcloud.webservice3.resources import (
    BusinessResource,
    ComponentModelResource,
    VariableModelResource
)
from gcloud.commons.template.resources import CommonTemplateResource
from gcloud.tasktmpl3.resources import (
    TaskTemplateResource,
    TemplateSchemeResource,
)
from gcloud.taskflow3.resources import TaskFlowInstanceResource
from gcloud.contrib.appmaker.resources import AppMakerResource
from gcloud.contrib.function.resources import FunctionTaskResource
from gcloud.periodictask.resources import PeriodicTaskResource

v3_api = Api(api_name='v3')
v3_api.register(BusinessResource())
v3_api.register(TaskTemplateResource())
v3_api.register(ComponentModelResource())
v3_api.register(VariableModelResource())
v3_api.register(TemplateSchemeResource())
v3_api.register(TaskFlowInstanceResource())
v3_api.register(AppMakerResource())
v3_api.register(FunctionTaskResource())
v3_api.register(PeriodicTaskResource())
v3_api.register(CommonTemplateResource())

# Standard bits...
urlpatterns = [
    url(r'^api/', include(v3_api.urls)),
]
