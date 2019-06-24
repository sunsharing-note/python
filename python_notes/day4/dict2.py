#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dict2.py
@Time    :   2018/12/16 16:46:36
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib


dic = {"name": {"name": ["huahua","zhouzhou"]}, "age": 22, "sex": "male", "company": "xiyangxixi"}
#del dic["name"]
#dic.pop("age") 删除键值对，并返回值
#dic.popitem() #随机删除一组简直对 并以元组方式返回
#dic1 = dict.fromkeys(["name","age"], "test")

#字典可以嵌套
print(dic)
#print(dic1)
#print(dic.clear()) #清空字典
print(sorted(dic.items()))

for i in dic:
    print(i, dic[i])