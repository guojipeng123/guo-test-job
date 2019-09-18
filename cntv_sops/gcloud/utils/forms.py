# -*- coding: utf-8 -*-
import json
import functools

from django import forms
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def post_form_validator(form_cls):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            form = form_cls(request.POST)
            if not form.is_valid():
                return JsonResponse(status=400, data={
                    'result': False,
                    'message': form.errors
                })
            setattr(request, 'form', form)
            return func(request, *args, **kwargs)

        return wrapper

    return decorate


class JsonField(forms.CharField):
    default_error_messages = {
        'invalid': _('invalid json string'),
    }

    def validate(self, value):
        super(JsonField, self).validate(value)

        try:
            json.loads(value)
        except Exception:
            raise ValidationError(
                self.error_messages['invalid'],
                code='invalid')
        else:
            return value


class JsonListField(JsonField):
    default_error_messages = {
        'invalid': _('json.loads result is not instance of list or tuple '),
    }

    def validate(self, value):
        super(JsonListField, self).validate(value)

        data = json.loads(value)

        if not isinstance(data, (list, tuple)):
            raise ValidationError(
                self.error_messages['invalid'],
                code='invalid')

        return value


class JsonDictField(JsonField):
    default_error_messages = {
        'invalid': _('json.loads result is not list'),
    }

    def validate(self, value):
        super(JsonListField, self).validate(value)

        data = json.loads(value)

        if not isinstance(data, dict):
            raise ValidationError(
                self.error_messages['invalid'],
                code='invalid')

        return value
