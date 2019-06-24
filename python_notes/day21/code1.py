#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

file = path.join(path.dirname(__file__),"readme.md")
f = open(file,"r",encoding="utf8")

print(f.read())
print("夕阳西下")