# -*- coding: utf-8 -*-
import ujson as json
from django import forms


class PeriodicTaskEnabledSetForm(forms.Form):
    enabled = forms.BooleanField(
        required=False,
        initial=False
    )


class JSONField(forms.CharField):
    def __init__(self, assert_type=None, type_string='', *args, **kwargs):
        self.assert_type = assert_type
        self.type_string = type_string
        super(JSONField, self).__init__(*args, **kwargs)

    def validate(self, value):
        super(JSONField, self).validate(value)
        try:
            json_val = json.loads(value)
        except Exception:
            raise forms.ValidationError('invalid json string', code='invalid')

        if self.assert_type and not isinstance(json_val, self.assert_type):
            raise forms.ValidationError('this json string must a %s' % self.type_string, code='invalid')

    def clean(self, value):
        value = super(JSONField, self).clean(value)
        return json.loads(value)


class PeriodicTaskCronModifyForm(forms.Form):
    cron = JSONField(
        assert_type=dict,
        type_string='object',
        required=True,
    )


class PeriodicTaskConstantsModifyForm(forms.Form):
    constants = JSONField(
        assert_type=dict,
        type_string='object',
        required=True
    )
