# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging
import traceback

from django.db import models
from django.utils.translation import ugettext_lazy as _

from pipeline.engine.conf import function_switch

logger = logging.getLogger('celery')


class FunctionSwitchManager(models.Manager):
    def init_db(self):
        try:
            name_set = {s.name for s in self.all()}
            s_to_be_created = []
            for switch in function_switch.switch_list:
                if switch['name'] not in name_set:
                    s_to_be_created.append(FunctionSwitch(
                        name=switch['name'],
                        description=switch['description'],
                        is_active=switch['is_active']
                    ))
                else:
                    self.filter(name=switch['name']).update(description=switch['description'])
            self.bulk_create(s_to_be_created)
        except Exception as e:
            logger.error('function switch init failed: %s' % traceback.format_exc(e))

    def is_frozen(self):
        return self.get(name=function_switch.FREEZE_ENGINE).is_active

    def freeze_engine(self):
        self.filter(name=function_switch.FREEZE_ENGINE).update(is_active=True)

    def unfreeze_engine(self):
        self.filter(name=function_switch.FREEZE_ENGINE).update(is_active=False)


class FunctionSwitch(models.Model):
    name = models.CharField(_(u"功能名称"), max_length=32, null=False, unique=True)
    description = models.TextField(_(u"功能描述"), default='')
    is_active = models.BooleanField(_(u"是否激活"), default=False)

    objects = FunctionSwitchManager()
