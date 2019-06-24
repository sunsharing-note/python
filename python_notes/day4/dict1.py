#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dict1.py
@Time    :   2018/12/16 15:48:44
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

dic = {"name": "huahua", "age": 22, "sex": "male", "company": "xiyangxixi"}
dic1 = {"name": "zhouzhou", "age": 25}
print(dic)

dic["name"] = "zhouzhou" #有则修改，无则添加
print(dic)

dic["hunyin"] = "weihun"
print(dic)

dic.setdefault("age", 34) #可以用来添加，有返回值的，返回key对应的真实的值
print(dic)

print(list(dic.keys())) #转换为list 获取所有keys
print(list(dic.values()))#获取所有值
print(list(dic.items()))

dic.update(dic1)
print(dic)