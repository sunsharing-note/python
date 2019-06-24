#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# here put the import lib

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

# sql = "select * from test"
# # 受影响的行
# reCount = cur.execute(sql)
# print(reCount)
#
# data = cur.fetchall()
# print(data)

# 批量插入     如果是单次插入 param=(10,"jiangjiang",1)
sql = "insert into test values(%s,%s,%s)"
params = [(4,"fanfan",1),(5,"meimei",0)]
reCount = cur.executemany(sql,params)

conn.commit()




cur.close()
closeConn(conn)
















