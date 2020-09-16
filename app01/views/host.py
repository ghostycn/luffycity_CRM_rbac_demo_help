#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponse,reverse
from app01 import models
from app01.forms.host import HostModelForm,UpdateHostModelForm
from rbac.service.urls import memory_reverse

def host_list(request):
    """
    主机列表
    :param request:
    :return:
    """
    if request.method == "GET":
        host_queryset = models.Host.objects.all()
        return render(request,'host_list.html',{"host_queryset":host_queryset})

def host_add(request):
    """
    添加主机
    :param request:
    :return:
    """
    if request.method == "GET":
        form = HostModelForm()
        return render(request, 'rbac/change.html', {"form":form})
    form = HostModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request,'host_list'))
    return render(request, 'rbac/change.html', {"form": form})

def host_edit(request,pk):
    """
    编辑主机
    :param request:
    :param pk:
    :return:
    """
    obj = models.Host.objects.filter(id=pk).first()

    if not obj:
        return HttpResponse("用户不存在")
    if request.method == "GET":
        form = UpdateHostModelForm(instance=obj)
        return render(request, 'rbac/change.html', {"form":form})
    form = UpdateHostModelForm(instance=obj,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(memory_reverse(request,'host_list'))
    return render(request, 'rbac/change.html', {"form": form})

def host_del(request,pk):
    """
    删除主机
    :param request:
    :param pk:
    :return:
    """
    origin_url = memory_reverse(request,'host_list')
    if request.method == "GET":
        return render(request,'rbac/delete.html',{"cancel":origin_url})
    elif request.method == "POST":
        models.Host.objects.filter(id=pk).delete()
        return redirect(origin_url)



