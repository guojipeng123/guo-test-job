# -*- coding: utf-8 -*-
from __future__ import absolute_import
import zlib

try:
    import cPickle as pickle
except ImportError:
    import pickle

from django.db import models


class IOField(models.BinaryField):
    def __init__(self, compress_level=6, *args, **kwargs):
        super(IOField, self).__init__(*args, **kwargs)
        self.compress_level = compress_level

    def get_prep_value(self, value):
        value = super(IOField, self).get_prep_value(value)
        return zlib.compress(pickle.dumps(value), self.compress_level)

    def to_python(self, value):
        try:
            value = super(IOField, self).to_python(value)
            return pickle.loads(zlib.decompress(value))
        except ImportError as e:
            return "IOField to_python raise error: %s" % e

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)
