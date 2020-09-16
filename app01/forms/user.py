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

class UserModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码")

    class Meta:
        model = models.UserInfo
        fields = ["name","password","confirm_password","email","phone","level","depart","roles"]

    def clean_confirm_password(self):
        """
        检查密码是否一致
        :return:
        """

        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError("两次输入的密码不一致")
        return confirm_password

class UpdateUserModelForm(BootStrapModelForm):

    class Meta:
        model = models.UserInfo
        fields = ["name","password","email","phone","level","depart","roles"]

    # def clean_name(self):
    #     name = self.cleaned_data["name"]
    #     obj = models.UserInfo.objects.filter(name=name)
    #     if obj:
    #         raise ValidationError("用户名已经存在")
    #     return name

class ResetPasswordUserModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码")

    class Meta:
        model = models.UserInfo
        fields = ["password","confirm_password"]




    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            raise ValidationError("两次密码数据不一致")
        return confirm_password