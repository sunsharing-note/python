#! /usr/bin/env python
# -*- coding: utf-8 -*-

from  fabric.api import  *
from fabric.contrib.files import *

def ff(hostss,config_path):
    x = 0
    re = []
    hostslist = []
    with open(r"%s" %config_path) as t:
        for i in t:
            hostslist.append(i.strip("\n"))
        for i in hostslist:
            if hostss in i:
                x += 1
                continue
            if x == 1:
                if "[" in i:
                    break
                re.append(i.strip("\n"))
        print(hostslist)
        print(re)
ff("portal53808183","./fab4.txt")
