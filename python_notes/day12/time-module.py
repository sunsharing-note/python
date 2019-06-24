#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import time
import datetime
#print(help(time))

# 带*****是的是必须掌握的
#print(time.time()) # 时间戳 *****
#print(time.clock()) # cpu执行时间
#print(time.sleep(3)) # 休眠 *****
'''print(time.gmtime()) # 时区时间
b = time.localtime()
print(b) # 本地时间 ***** mtime ctime
a = time.strftime("%Y%m%d", time.localtime())
print(a)
'''
c = datetime.datetime.now()
print(c)
'''
d = time.strptime("2019-01-04", "%Y-%m-%d")
print(d)
print(d.tm_year)'''