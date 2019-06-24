#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Foo:
    def bar(self):
        print("bar")

obj = Foo()
# obj.bar()
Foo.bar(obj)