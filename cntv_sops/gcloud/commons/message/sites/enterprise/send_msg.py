# -*- coding: utf-8 -*-
import json
import logging

from gcloud.core.utils import get_client_by_user_and_biz_id

logger = logging.getLogger("root")


def send_message(biz_cc_id, executor, notify_type, receivers, title, content):
    client = get_client_by_user_and_biz_id(executor, biz_cc_id)
    if 'weixin' in notify_type:
        kwargs = {
            'receiver__username': receivers,
            'data': {
                'heading': title,
                'message': content,
            }
        }
        result = client.cmsi.send_weixin(kwargs)
        if not result['result']:
            logger.error('taskflow send weixin, kwargs=%s, result=%s' % (json.dumps(kwargs),
                                                                         json.dumps(result)))
    if 'sms' in notify_type:
        kwargs = {
            'receiver__username': receivers,
            'content': u"%s\n%s" % (title, content),
        }
        result = client.cmsi.send_sms(kwargs)
        if not result['result']:
            logger.error('taskflow send sms, kwargs=%s, result=%s' % (json.dumps(kwargs),
                                                                      json.dumps(result)))

    if 'email' in notify_type:
        kwargs = {
            'receiver__username': receivers,
            'title': title,
            'content': content,
        }
        result = client.cmsi.send_mail(kwargs)
        if not result['result']:
            logger.error('taskflow send mail, kwargs=%s, result=%s' % (json.dumps(kwargs),
                                                                       json.dumps(result)))

    if 'voice' in notify_type:
        kwargs = {
            'receiver__username': receivers,
            'auto_read_message': u"%s\n%s" % (title, content),
        }
        result = client.cmsi.send_voice_msg(kwargs)
        if not result['result']:
            logger.error('taskflow send voice, kwargs=%s, result=%s' % (json.dumps(kwargs),
                                                                        json.dumps(result)))

    return True
