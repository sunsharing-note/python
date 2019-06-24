#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

f = open("json_test.txt","r")

# 加载出来显示
data = json.loads(f.read())

f.close()
print(data["name"])


