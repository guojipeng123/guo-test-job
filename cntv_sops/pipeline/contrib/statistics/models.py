# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ComponentInTemplate(models.Model):
    component_code = models.CharField(_(u"组件编码"), max_length=255)
    template_id = models.CharField(_(u"模板ID"), max_length=32)
    node_id = models.CharField(_(u"节点ID"), max_length=32)
    is_sub = models.BooleanField(_(u"是否子流程引用"), default=False)
    subprocess_stack = models.TextField(_(u"子流程堆栈"), default="[]", help_text=_(u"JSON 格式的列表"))

    class Meta:
        verbose_name = _(u"Pipeline原子被引用数据")
        verbose_name_plural = _(u"Pipeline原子被引用数据")

    def __unicode__(self):
        return u"%s_%s" % (self.component_code, self.template_id)


class ComponentExecuteData(models.Model):
    component_code = models.CharField(_(u"组件编码"), max_length=255)
    instance_id = models.CharField(_(u"实例ID"), max_length=32)
    node_id = models.CharField(_(u"节点ID"), max_length=32)
    is_sub = models.BooleanField(_(u"是否子流程引用"), default=False)
    subprocess_stack = models.TextField(_(u"子流程堆栈"), default="[]", help_text=_(u"JSON 格式的列表"))
    started_time = models.DateTimeField(_(u"原子执行开始时间"))
    archived_time = models.DateTimeField(_(u"原子执行结束时间"), null=True, blank=True)
    elapsed_time = models.IntegerField(_(u"原子执行耗时(s)"), null=True, blank=True)
    status = models.BooleanField(_(u"是否执行成功"), default=False)
    is_skip = models.BooleanField(_(u"是否跳过"), default=False)
    is_retry = models.BooleanField(_(u'是否重试记录'), default=False)

    class Meta:
        verbose_name = _(u"Pipeline原子执行数据")
        verbose_name_plural = _(u"Pipeline原子执行数据")
        ordering = ["-id"]

    def __unicode__(self):
        return u"%s_%s" % (self.component_code, self.instance_id)


class TemplateInPipeline(models.Model):
    template_id = models.CharField(_(u"模板ID"), max_length=255)
    atom_total = models.IntegerField(_(u"原子总数"))
    subprocess_total = models.IntegerField(_(u"子流程总数"))
    gateways_total = models.IntegerField(_(u"网关总数"))

    class Meta:
        verbose_name = _(u"Pipeline模板引用数据")
        verbose_name_plural = _(u"Pipeline模板引用数据")

    def __unicode__(self):
        return u"%s_%s_%s_%s" % (self.template_id, self.atom_total, self.subprocess_total, self.gateways_total)


class InstanceInPipeline(models.Model):
    instance_id = models.CharField(_(u"实例ID"), max_length=255)
    atom_total = models.IntegerField(_(u"原子总数"))
    subprocess_total = models.IntegerField(_(u"子流程总数"))
    gateways_total = models.IntegerField(_(u"网关总数"))

    class Meta:
        verbose_name = _(u"Pipeline实例引用数据")
        verbose_name_plural = _(u"Pipeline实例引用数据")

    def __unicode__(self):
        return u"%s_%s_%s_%s" % (self.instance_id, self.atom_total, self.subprocess_total, self.gateways_total)