#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   str2.py
@Time    :   2018/12/16 20:58:43
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

str1 = "hello world,Let's go {name}"
print(str1.count("l"))
print(str1.capitalize()) #首字母大写
print(str1.center(50,"#")) #居中
print(str1.endswith("go")) #以什么结尾
print(str1.startswith("he")) #以什么开头
print(str1.expandtabs(tabsize=5)) #多少空格
print(str1.find("he"))#查找字符，返回其索引
print(str1.format(name="huahua"))#格式化
print(str1.format_map({"name": "zhouzhou"}))#格式化，通过字典
print(str1.index("hello"))#返回索引
print(str1.isalnum())
print("00001".isdecimal())
print("123456.123".isdigit())#判断是否是整形
print("12345.123".isalpha())
print("1234.444".isnumeric())
print("123abcd".isidentifier())#是否合法
print("abdUp".islower())
print("adacds1234".isupper())
print(str1.istitle()) #每个单词是否以大写开头
print("    e".isspace())
print(str1.lower())
print(str1.upper())
print(str1.swapcase()) #大写变小写，小写变大写
print(str1.ljust(50,"#"))#右边加
print(str1.rjust(50,"#"))#左边加
print("   My Title\ntest".strip())
print("My title tilte".replace("title","dear",1))
print("My title title".rfind("t"))#返回真是索引位置
print("My title title".split(" "))
print("My title title".rsplit("i",2))#分割几次，从右往左走
#str2 = str1.isupper()
#print(str2)