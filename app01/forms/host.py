#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from app01 import models
from django.core.exceptions import ValidationError

class BootStrapModelForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(BootStrapModelForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

class HostModelForm(BootStrapModelForm):

    class Meta:
        model = models.Host
        fields = "__all__"



class UpdateHostModelForm(BootStrapModelForm):

    class Meta:
        model = models.Host
        fields = "__all__"

    # def clean_name(self):
    #     name = self.cleaned_data["name"]
    #     obj = models.UserInfo.objects.filter(name=name)
    #     if obj:
    #         raise ValidationError("用户名已经存在")
    #     return name
