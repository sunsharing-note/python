#! /usr/bin/env python
# -*- coding: utf-8 -*-



import pymysql


conn = pymysql.connect(host="xxx",port=3306,user="root",passwd="root",db="huahua",charset="utf8")
cursor = conn.cursor()
a = 2
b = "女"
c = 1
# 添加数据 使用参数传入方式 防止SQL注入

# 查询时 fetchall返回的是一个元组里面套的一个元组，fetchone返回的直接是一个元组
sql = 'insert into test values(%s,%s,%s)'
# 传入一个元组
ll = [(4,"fanfan",1),(5,"meimei",0)]
# sql = 'insert into test values(1,"男",1)'

# 绝对
# cursor.scroll(0,mode="absolute")
#
# # 相对
# cursor.scroll(1,mode="relative")
cursor.executemany(sql,ll)

# 受影响行数
# r = cursor.execute(sql)

# print(r)
conn.commit()

cursor.close()

conn.close()