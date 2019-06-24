#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   list1.py
@Time    :   2018/12/15 21:54:12
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
x = [1, 2, 5, 3, 6, 4, 10]
x.sort(reverse=True) #排序
print(x)

tp = type(x)
print(tp)
'''
a = ["test1", "test2", "test3", "test4", "test3"]
a.reverse() #首尾颠倒
print(a)

first_index = a.index("test3")
b = a[first_index+1:]
second_index = b.index("test3")
index = first_index + second_index + 1
print(index)

b = ["test6", "test7"]
a.extend(b)# 扩展a

idex = a.index("test1")
print(a)
print(b)
print(idex)
#print(a.count("test1"))


a.append("test6")
a.remove("test6") #除了remove 还可以使用pop delete
a.insert(1, "test7") #增加到index为1的值之前
idx = a.index("test2")
a[1:3] = ["huahua", "zhouzhou"]
a.pop(1) #删掉之后会返回删除的值 可先用变量存下来，再打印出来
del a[0] #可以删除固定值或者整个列表
print(a)
print(a[1:]) #取到最后
print(a[1:-1]) #取到倒数第二个
print(a[1:-1:2]) #从左到右 步长为2
print(a[3::-2]) # 从右往左走 最后的数代表了从哪个方向开始取
print(idx)'''