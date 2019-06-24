#! /usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import time
#
# time_tup = time.time()
# print((time_tup))
# t1 = "2019-01-14 00:00:00"
#
# time_tup2 = time.mktime(time.strptime(t1,'%Y-%m-%d %H:%M:%S'))
# print(time_tup2)

import datetime
import time

now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 当前时间的时间戳
# timeArray1 = time.strptime(now_time,"%Y-%m-%d %H:%M:%S")
timeArray1 = time.strptime(now_time,"%Y-%m-%d %H:%M:%S")
timeStamp1 = time.mktime(timeArray1)
print(now_time,timeStamp1)
# path = os.path.dirname(os.path.abspath(__file__))
# ss = path.join("/test.txt")
# print(ss)