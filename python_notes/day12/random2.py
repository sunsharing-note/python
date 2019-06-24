#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

'''
def code():
    code = ""
    for i in range(5):
        if i == random.randint(0,3):
            add = random.randrange(10)
        else:
            add = chr(random.randrange(65,91))
        code += str(add)
code()'''

def code():
    code = ""
    for i in range(5):
        add = random.choice([random.randrange(10),chr(random.randrange(65,91))])
        '''
        if i == random.randint(0,3):
            add = random.randrange(10)
        else:
            add = chr(random.randrange(65,91))'''
        code += str(add)
    print(code)
code()