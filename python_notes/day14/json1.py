#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

dic = {"name": "huahua", "sex": "male","age": "19"}

# 加载进去
data = json.dumps(dic)

f = open("json_test.txt","w")

f.write(data)

f.close()

# 保存后的不是字典