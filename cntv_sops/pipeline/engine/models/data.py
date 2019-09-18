# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pipeline.engine.models.fields import IOField


class DataSnapshotManager(models.Manager):
    def set_object(self, key, obj):
        self.update_or_create(key=key,
                              defaults={
                                  'obj': obj
                              })
        return True

    def get_object(self, key):
        try:
            return self.get(key=key).obj
        except DataSnapshot.DoesNotExist:
            return None

    def del_object(self, key):
        try:
            self.get(key=key).delete()
            return True
        except DataSnapshot.DoesNotExist:
            return False


class DataSnapshot(models.Model):
    key = models.CharField(_(u"对象唯一键"), max_length=255, primary_key=True)
    obj = IOField(verbose_name=_(u"对象存储字段"))

    objects = DataSnapshotManager()
