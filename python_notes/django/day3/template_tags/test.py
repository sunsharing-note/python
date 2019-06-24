#! /usr/bin/env python
# -*- coding: utf-8 -*-


from django import template

from django.utils.safestring import mark_safe

register = template.Library()

# @register.filter()
@register.simple_tag
def add(v1):
    return v1 + 100

# 然后再html中引入:{% load test %}