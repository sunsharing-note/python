#! /usr/bin/env python
# -*- coding: utf8 -*-

# while True:
#     try:
#         inp = input("请输入序号：")
#         i = int(inp)
#     except Exception as e:
#         i = 1
#     finally:
#         print("xxxxxxx")
#     print(i)

try:
    raise Exception("xxxxxxxx")
except Exception as e:
    print(e)