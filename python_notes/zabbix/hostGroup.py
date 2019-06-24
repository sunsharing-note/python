#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

def getHostGroup(url,header,token):
    data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend"
    },
    "auth": token,
    "id": 1
}
    group = requests.post(url=url,headers=header,data=json.dumps(data))
    return json.loads(group.content)["result"]

url = "http://xxxxxxxx/zabbix/api_jsonrpc.php"

header = {"Content-Type": "application/json-rpc"}
token = "8e7a35dfd858dfa88f41c3565114e479"

print(getHostGroup(url,header,token))
