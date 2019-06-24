#! /usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
#from datetime import datetime


env.user = "root"
env.password = "123456"
env.hosts = ["192.168.29.101"]


def deploy():
    #远程目录
    remote_tomcat_dir = "/data/tomcat/"
    #remote_tomcat_dir = "/data/tomcat/apache-tomcat-8.0.45.tar.gz"
    remote_tomcat_start = "/data/tomcat/"
    run("ps -ef |grep java |grep -v grep |awk '{print $2}' |xargs kill -9 ")
    run("cd %s && rm -rf *" % remote_tomcat_dir)
    put("apache-tomcat-8.0.45.tar.gz",remote_tomcat_dir)
    with cd(remote_tomcat_start):
        run("tar -zxvf apache-tomcat-8.0.45.tar.gz")
        run("set -m;%sapache-tomcat-8.0.45/bin/catalina.sh start"% remote_tomcat_start)