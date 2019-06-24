#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pymysql
import re

host = "xxxx"
user = "root"
password = "root"
db = "mysql"

def getConn(host,user,password,db):
    try:
        conn = pymysql.connect(host=host,user=user,password=password,db=db)
        return conn
    except Exception as e:
        print("Error %d: %s" %(e.args[0],e.args[1]))
        sys.exit(1)

def closeConn(conn):
    conn.close()


def getValue(conn,query):
    cursor = conn.cursor()
    getNum = cursor.execute(query)
    if getNum>0:
        result = cursor.fetchone()
        print(result)
    else:
        result=['0']
    return int(result[1])

def getQuery(conn,query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return  result

# 执行查询数量
Questions = "show global status like 'Questions'"
# 开机时间
Uptime = "show global status like 'Uptime'"
# commit
Com_commit = "show global status like 'Com_commit'"
# rollback
Com_rollback = "show global status like 'Com_rollback'"
# 每秒查询
Com_select = "show global status like 'Com_select'"
def writeFile(select,value):
    with open("%s.txt" %(select),"w",encoding="utf8") as f:
        f.write("%s" %(value))

def getSelect(Questions):
    select = str(re.findall("('.*')",Questions))
    return select[3:-3]



if __name__ == "__main__":
    conn=getConn(host,user,password,db)
    writeFile(getSelect(Questions),getValue(conn,Questions))
    writeFile(getSelect(Uptime),getValue(conn,Uptime))
    closeConn(conn)




