#! /usr/bin/env python
# -*- coding: utf8 -*-


import subprocess
a = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE)
print(str(a.stdout.read(),"gbk"))