#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import re
s = "hello world"

# t = re.findall("w...d", s)
# print(t) # 全匹配

t = re.findall("^h...o", "he;;;;") # 以什么开始

print(t)

print(re.findall("alix$", "hello alix")) # 以什么结尾

print(re.findall("fds.*ksf","hsafdsfafrqfqr=gnvkcnaksf")) # .* *表示匹配前面的字符0此或多次
print(re.findall("a{5}b", "aaaaab"))
print(re.findall("a{1,3}b", "aaab")) # 贪婪匹配
print(re.findall("a[bcd]", "ab")) # []中额内容选择一个 或的关系
print(re.findall("[1-9a-zA-Z]","12stAZ"))
print(re.findall("[^4,5]","456sz")) # 4 5 都不会有
print(re.findall("\sasd", "fak asd"))
print(re.findall(r"I\b", "hello, I am a tI$est"))
print(re.search("sb", "hello sb").group()) # 匹配出满足条件的第一个
#print(re.findall("\\c","abcdd\c"))
print(re.findall("\\\\d","asbcd\d"))
print(re.findall(r"\\d", "abcd\d"))
print(re.findall(r"\bblow","blow"))

print(re.findall("(as)+", "fsfadfaasas"))
print(re.search("(as)+", "abcdasasas").group())
print(re.search("(as)|3", "as3").group())

# ?P<id>取名字 后面可以单独取id或者name
print(re.search("(?P<id>\d{3})/(?P<name>\w{3})", "sfsdfadfa123/ooo").group("name"))