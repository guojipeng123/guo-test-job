# -*- coding: utf-8 -*-

from django import forms


class ConfigForm(forms.Form):
    executor = forms.CharField(
        required=False
    )
    always_use_executor = forms.BooleanField(
        required=False,
        initial=False
    )
