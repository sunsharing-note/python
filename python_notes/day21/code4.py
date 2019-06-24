#! /usr/bin/env python
# -*- coding: utf-8 -*-


import json

s = "苑浩" # unicode

# b1 = s.encode("utf8")
# print(b1,type(b1))
# print(b1.decode("utf8"))
# print(b1.decode("gbk"))

print(json.dumps(s)) # unicode
print(bytes(s,encoding="utf8"))