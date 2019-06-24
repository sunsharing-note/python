#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 远程执行

from fabric.api import *



env.user = "root"
env.password = "123456"
# 用户名和密码一样
# env.hosts=['user@ip:port',]
env.hosts = ["192.168.29.101","192.168.29.102"]
# 密码不一样
# env.passwords={'root@192.168.56.1:22':'passwd', 'root@192.168.56.2:22':'python'}
# 不同主机不同密码
"""
env.hosts = [
    'root@192.168.10.201:22',
    'root@192.168.10.202:22',
    'root@192.168.10.203:22'
]
env.passwords = {
    'root@192.168.10.201:22':'123456201',
    'root@192.168.10.202:22':'123456202',
    'root@192.168.10.203:22':'123456203'
"""

def getHostname():
    run("hostname")