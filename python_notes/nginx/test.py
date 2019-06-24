#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

while True:
    try:
        ret = os.popen("netstat -ant |awk '{print $6}|sort -r|uniq -c|sort -rn,cmd'").readlines()
        print(ret)
        sys.exit(0)
    except Exception as e:
        print strftime("%Y-%m-%r %H:%M")
        sys.exit(0)