#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import re

print(re.match("asd", "asdfhdasd").group())

print(re.split("[k]","djksal"))
print(re.split("[k,s]","djksal"))  # 先通过K分 再通过s分 如果s前面没东西，则分之后为空

print(re.sub("a","x","asdabc")) # 替换

r = re.compile("\.com")
print(r.findall("www.baidu.comxxxxx"))