#! /usr/bin/env python
# -*- coding: utf-8 -*-

from forms import AssetForm
from django.shortcuts import render_to_response
from models import Host, HostGroup
from forms import GroupForm, IdcForm


def group(request):
    temp_name = "cmdb/cmdb-header.html"
    allgroup = HostGroup.objects.all()
    return render_to_response('cmdb/group.html', locals())


def group_add(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render_to_response("cmdb/group_add.html", locals())
    else:
        display_control = "none"
        group_form = GroupForm()
        idc_form = IdcForm()
        return render_to_response("cmdb/group_add.html", locals())


def group_add_mini(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == "POST":
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group_form.save()
            tips = u"增加成功！"
            display_control = ""
            status = 1
        else:
            tips = u"增加失败！"
            display_control = ""
        return render_to_response("cmdb/group_add_mini.html", locals())
    else:
        display_control = "none"
        group_form = GroupForm()
        return render_to_response("cmdb/group_add_mini.html", locals())


def group_del(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == 'POST':
        group_items = request.POST.getlist('g_check', [])
        if group_items:
            for n in group_items:
                HostGroup.objects.filter(id=n).delete()
    allgroup = HostGroup.objects.all()
    return render_to_response("cmdb/group.html", locals())


def group_edit(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == 'GET':
        groupid = request.GET.get("id")
        obj = HostGroup.objects.get(id=groupid)
        allgroup = HostGroup.objects.all()
    return render_to_response("cmdb/group_edit.html", locals())


def group_save(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == 'POST':
        group_id = request.POST.get('id')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        group_item = HostGroup.objects.get(id=group_id)
        group_item.name = name
        group_item.desc = desc
        group_item.save()
        obj = group_item
        status = 1
    else:
        status = 2
    return render_to_response("cmdb/group_edit.html", locals())