#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

dic = {"name": "huahua", "sex": "male","age": "19"}

# 加载进去


f = open("json_test2.txt","w")

json.dump(dic,f)

f.close()

# 保存后的不是字典