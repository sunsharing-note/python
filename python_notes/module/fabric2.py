#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 本地执行
from fabric.api import local

def test():
    local("cd /data && ls -al")

