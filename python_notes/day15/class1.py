#!/usr/bin/env python
# -*- coding: utf-8 -*-


class foo:
    def test(self,name,sex):
        print(name,sex)
        return 1


obj = foo()

t1 = obj.test("huahua","male")
print(t1)