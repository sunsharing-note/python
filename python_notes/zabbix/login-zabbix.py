#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import re
# import time
# import datetime


# 获取登录token
def getToken(url, header, username, password):
    data = {"jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": username,
                "password": password
            },
            "id": 1,
            "auth": None
            }
    request = requests.post(url=url, headers=header, data=json.dumps(data))
    return json.loads(request.content)["result"]


# 获取所有主机
def getHost(url, header, token):
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },
        "id": 2,
        "auth": token
    }
    # print(token)
    # hosss = requests.post(url=url,headers=header,data=json.dumps(data))
    # return json.loads(hosss.content)["result"]
    hosts = requests.post(url=url, headers=header, data=json.dumps(data))
    return json.loads(hosts.content)["result"]


# 获取所有ip
def getIp(hosts):
    ret = re.findall("(\d{1,3}\.\d+\.\d+\.\d+)", hosts)
    return ret


# 写到hosts.txt文件中
def writeHost(host):
    with open("hosts.txt", "a", encoding="utf8") as  ho:
        host = list(set(host))
        host.sort()
        for i in host:
            ho.write("%s\n" % i)


# 获取sla
def getSla(url, header, token):
    data = {
        "jsonrpc": "2.0",
        "method": "service.getsla",
        "params": {
            "serviceids": "2",
            "intervals": [
                {
                    "from": xxxx ,
                    "to": xxxx
                }
            ]
        },
        "auth": token,
        "id": 1
    }

    sla = requests.post(url=url, headers=header, data=json.dumps(data))
    return json.loads(sla.content)["result"]


url = "http://xxxxxxxxx/zabbix/api_jsonrpc.php"
#url = "https://xxxxxxxxxxx/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json-rpc"}
username = "xxxxxxxx"
password = "xxxxxxxxxx"
token = getToken(url, header, username, password)
print(token)
# print(token)
# print(url)
# 返回所有主机
hosts = str(getHost(url, header, token))
# print(hosts)
# print(type(hosts))
# 返回所有主机ip
host = getIp(hosts)
# print(host)
# 写进文本中
#writeHost(host)
# t1 = time.time()
# #from_time = "2019-01-14 00:00:00"
# now_time = datetime.datetime.now()
# before_time = now_time + datetime.timedelta(days=-7)
# t2 = time.mktime(time.strptime(str(before_time),'%Y-%m-%d %H:%M:%S'))
#
#
#
#
#
#print(getSla(url,header,token,t1,t2))
