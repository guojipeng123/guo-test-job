# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class LogEntryManager(models.Manager):
    def link_history(self, node_id, history_id):
        self.filter(node_id=node_id, history_id=-1).update(history_id=history_id)

    def plain_log_for_node(self, node_id, history_id):
        entries = self.order_by('id').filter(node_id=node_id, history_id=history_id)
        plain_entries = []
        for entry in entries:
            plain_entries.append('[%s %s] %s, exception: %s' % (entry.logged_at.strftime('%Y-%m-%d %H:%M:%S'),
                                                                entry.level_name,
                                                                entry.message,
                                                                entry.exception))
        return '\n'.join(plain_entries)

    def delete_expired_log(self, interval):
        expired_date = timezone.now() + timezone.timedelta(days=(-interval))
        to_be_deleted = self.filter(logged_at__lt=expired_date)
        count = to_be_deleted.count()
        to_be_deleted.delete()
        return count


class LogEntry(models.Model):
    objects = LogEntryManager()

    logger_name = models.SlugField(_(u"logger 名称"), max_length=128)
    level_name = models.SlugField(_(u"日志等级"), max_length=32)
    message = models.TextField(_(u"日志内容"), null=True)
    exception = models.TextField(_(u"异常信息"), null=True)
    logged_at = models.DateTimeField(_(u"输出时间"), auto_now_add=True)

    node_id = models.CharField(_(u"节点 ID"), max_length=32, db_index=True)
    history_id = models.IntegerField(_(u"节点执行历史 ID"), default=-1)
