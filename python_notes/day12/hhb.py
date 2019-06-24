#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

# 加密模块 md5 sha sha256用得最多
import hashlib

m = hashlib.md5()
print(m)
m.update("hello world".encode("utf8"))
print(m.hexdigest())
m.update("huazai".encode("utf8"))
print(m.hexdigest())
m2 = hashlib.md5()
m2.update("hello worldhuazai".encode("utf8"))
print(m2.hexdigest())