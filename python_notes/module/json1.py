#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json

data1 = {'name': 'huazai', 'age': 21}

# dumps只进行反序列化为str
# dump必须传文件描述符，将序列化的str保存到文件中
# loads 只完成了反序列化
# load 只接收文件描述符，完成了读取文件和反序列化
d1 = json.dumps(data1)
d2 = json.dumps(data1,sort_keys=True)
d3 = json.dumps(data1,sort_keys=True)
d4 = json.dumps(data1,sort_keys=True,indent=4)



print(d1)
print(d2)
print(d3)
print(d4)

print(d1 == d2)
print(d2 == d3)

