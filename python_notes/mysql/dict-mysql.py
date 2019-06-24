#! /usr/bin/env python
# -*- coding: utf-8 -*-
import  pymysql
import  sys

host = "xxx"
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

# 创建cursor时就指定其返回dict类型数据
conn = getConn(host,user,password,db)
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

# sql = "select * from test"
#
# reCount = cur.execute(sql)
# print(reCount)
# data = cur.fetchall()
# print(data)

# 获取自增id
sql2 = "insert into test values(%s,%s,%s)"
param = (9,"tingting",1)
reCount = cur.execute(sql2,param)
conn.commit()
# 只有提交了才会有
new_id = cur.lastrowid
print(new_id)

cur.close()
closeConn(conn)