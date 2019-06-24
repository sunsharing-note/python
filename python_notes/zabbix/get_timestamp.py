#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

# t1 = time.time()
# #from_time = "2019-01-14 00:00:00"
# now_time = datetime.datetime.now()
# before_time = now_time + datetime.timedelta(days=-7)
# t2 = time.mktime(time.strptime(str(before_time),'%Y-%m-%d %H:%M:%S'))
now_time = datetime.datetime.now().strftime("%Y-%m-%d 00:00:00")
to_time = datetime.datetime.now()+ datetime.timedelta(days=-7)
to_time2 = to_time.strftime("%Y-%m-%d 00:00:00")
timeArray1 = time.strptime(now_time,"%Y-%m-%d %H:%M:%S")
timeStamp1 = time.mktime(timeArray1)
timeArray2 = time.strptime(to_time2,"%Y-%m-%d %H:%M:%S")
timeStamp2 = time.mktime(timeArray2)
#print(now_time)
#print(timeArray1)
print(timeStamp1)


# timeArray2= time.strptime(to_time,"%Y-%m-%d %H:%M:%S")
# timeStamp2 = time.mktime(timeArray2)
#
print(timeStamp2)
