#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import re

s = "1-2*((60-30+(-40/5)*(9-2*5/3))-6)"

def check(s):
    flag = True
    if re.findall("[a-zA-Z]",s):
        print("Invalid pattern")
        flag = False
    return flag

def cal_mul_div(s):
    ret = re.search("\d+\.?\d*[*/]\d+\.?\d*",s).group()
    #x, y = re.split("[*/]",ret) # 用字符串的split也可以
    # 判断*/ 用fload强转
    ret2 = float(float(x) * float(y))
    s.replace(re1,ret2)
    return s

def cal_add_sub(strs):

    return s

def format(s):
    s = s.replace(" ","")
    s = s.replace("++","+")
    return s

if check(s):
    strs = format(s)

    while re.search("\(",strs):
        strs = re.search("\([^()]+|)",strs).group()
        strs = cal_mul_div(strs)
        strs = cal_add_sub(strs) # '(20)' 利用strs[1:-1]
    else:
        strs = cal_mul_div(strs)
        strs = cal_add_sub(strs)