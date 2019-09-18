# -*- coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pipeline.component_framework.library import ComponentLibrary


class ComponentManager(models.Manager):
    def get_component_dict(self):
        """
        获得原子对应的dict类型
        :return:
        """
        components = self.filter(status=True)
        component_dict = {}
        for bundle in components:
            name = bundle.name.split('-')
            group_name = _(name[0])
            name = _(name[1])
            component_dict[bundle.code] = '%s-%s' % (group_name, name)
        return component_dict


class ComponentModel(models.Model):
    """
    注册的组件
    """
    code = models.CharField(_(u"组件编码"), max_length=255, unique=True)
    name = models.CharField(_(u"组件名称"), max_length=255)
    status = models.BooleanField(_(u"组件是否可用"), default=True)

    objects = ComponentManager()

    class Meta:
        verbose_name = _(u"组件 Component")
        verbose_name_plural = _(u"组件 Component")
        ordering = ['-id']

    def __unicode__(self):
        return self.name

    @property
    def group_name(self):
        return ComponentLibrary.get_component_class(self.code).group_name

    @property
    def group_icon(self):
        return ComponentLibrary.get_component_class(self.code).group_icon
