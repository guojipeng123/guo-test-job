# -- XXX This module must not use translation as that causes
# -- a recursive loader import!
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.utils import timezone


def make_aware(value):
    if settings.USE_TZ:
        # naive datetimes are assumed to be in UTC.
        if timezone.is_naive(value):
            value = timezone.make_aware(value, timezone.utc)
        # then convert to the Django configured timezone.
        default_tz = timezone.get_default_timezone()
        value = timezone.localtime(value, default_tz)
    return value


def now():
    return make_aware(timezone.now())
