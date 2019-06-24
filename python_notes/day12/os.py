#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


print(os.getcwd()) # 当前文件所在路径
# 如果加了r 表示原生字符串
#print(os.chdir("C:\python学习视频\python3教程 2017\day18-python 全栈开发-基础篇")) # 改变所在目录
# print(os.getcwd())
# print(os.curdir)
#print(os.pardir)
#print(os.makedirs("abc\\test")) # 递归生成文件夹
#print(os.removedirs("abc\\alex\\alvin")) #删除文件夹 只能删除空文件夹 有文件的不会删除 会往上一直找并删除符合的文件夹
#print(os.mkdir()) #创建单文件夹
#print(os.rmdir()) #删除单文件夹
print(os.listdir(".")) # 展示当前文件夹下的内容 包括文件夹以及文件
#print(os.remove("")) # 删除文件 不能删除文件夹
#print(os.rename("time.py","time-module.py")) #重命名文件或文件夹
print(os.stat("random2.py")) # 查看文件信息
print(os.stat("random2.py").st_mtime) # 获取该文件最后访问时间
#print(os.sep) # 路径连接符 win \ linux /
print(os.linesep) #换行分隔符 win \r\n linux \n
print(os.pathsep) #环境变量分割符 win ; linux :
print(os.system("dir")) # 执行命令
print(os.environ) #返回环境变量
print(os.path.abspath(".")) #返回给定路径的绝对路径
print(os.path.split("random2.py")) #分割给定路径的
print(os.path.dirname(".\\random2.py"))
print(os.path.dirname(os.path.abspath("random2.py")))
print(os.path.basename("random2.py"))
print(os.path.isfile("random2.py"))
print(os.path.isdir("random2.py"))
print(os.path.join()) #拼接路径