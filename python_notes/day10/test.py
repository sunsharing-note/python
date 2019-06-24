#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

def test():
    x = 10
    def inner():
        print(x)
    return inner

test()()  # inner被称为闭包