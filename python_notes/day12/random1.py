#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
def code():
    code = ''
    for i in range(5):
        add_num = random.randrange(10)
        code += str(add_num)
    print(code)
code()