#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import re

print(re.findall("a[bc]d", "abcd"))
print(re.findall("[.*+]", "a.cd+"))
print(re.findall("[^ab]", 'abcddf"ab"'))

print(re.findall(r"(ab)+", "abd"))

# 命名分组

print(re.search("(?P<id>\d{3})/(?P<name>\w{3})", "sfsdfadfa123/ooo").group("name"))

print(re.findall("www.(\w+).com", "www.huahua.com"))  # 只会返回huahua 也就是组里面的内容
print(re.findall("www.(?:\w+).com", "www.huahua.com"))  # 只会返回huahua 也就是组里面的内 ?:取消只显示组里面的内容

print(re.subn("a", "x", "asdabc"))  # 替换 返回替换了几次

print(next(re.finditer("\d", "ds224adfa4")).group())
