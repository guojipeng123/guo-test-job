# -*- coding: utf-8 -*-

from django import forms


class TemplateImportForm(forms.Form):
    override = forms.BooleanField(
        required=False,
        initial=False
    )
