#coding: utf-8
import json,urllib2
header = {"Content-Type": "application/json"}
ApiUrl = 'http://sxxxxxxxx/zabbix/api_jsonrpc.php'

class zabbixAuth(object):

    def __init__(self,user,passwd):
        self.user = user
        self.passwd = passwd

    def getAuth(self):
        data =json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.passwd,
            },
            "id":0
        })
        request = urllib2.Request(ApiUrl, data)
        for key in header:
            request.add_header(key, header[key])
        result = urllib2.urlopen(request)
        response = json.loads(result.read())
        result.close()
        print('auth:',response['result'])
        with open('auth.txt','w') as f:
            f.write(str(response['result']))
            f.close()


class zabbixAPi(object):

    with open('auth.txt','r') as f:
        auth = str(f.readline()).strip()
        f.close()
    def __init__(self):
        pass
    def zabbixRequest(self,method,params=None):
        request_json = json.dumps({
            'jsonrpc':"2.0",
            'method':method,
            'params':params or {},
            'auth':zabbixAPi.auth,
            'id':1,
        })
        request = urllib2.Request(ApiUrl,request_json)
        for key in header:
            request.add_header(key, header[key])
        result = urllib2.urlopen(request)
        response = json.loads(result.read())
        result.close()
        return response['result']


#user1auth = zabbixAuth('http://xxxxxx/api_jsonrpc.php','Admin','xxxxxx')








