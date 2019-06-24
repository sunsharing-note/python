#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

host = "xxxx"
user = "root"
password = "root"
db = "huahua"

def getConn(host,user,password,db):
    try:
        conn = pymysql.connect(host=host,user=user,password=password,db=db)
        return conn
    except Exception as e:
        print("Error %d: %s" %(e.args[0],e.args[1]))
        sys.exit(1)

def closeConn(conn):
    conn.close()

conn = getConn(host,user,password,db)
cur = conn.cursor()

sql = "select * from test"

cur.execute(sql)
# reCount = cur.execute(sql)
# print(reCount)

# cur.fetchone()
# data = cur.fetchone()
# print(data)


# data1 = cur.fetchone()
# print(data1)
#
# data2 = cur.fetchone()
# print(data2)

# 绝对定位
# cur.scroll(0,mode="absolute")
# data1 = cur.fetchone()
# print(data1)
#
# cur.scroll(0,mode="absolute")
# data2 = cur.fetchone()
# print(data2)
#
# data3 = cur.fetchone()
# print(data3)

# 相对定位
cur.scroll(-1,mode='relative')
data1 = cur.fetchone()
print(data1)

cur.scroll(-1,mode="relative")
data2 = cur.fetchone()
print(data2)

data3 = cur.fetchone()
print(data3)


cur.close()
closeConn(conn)
