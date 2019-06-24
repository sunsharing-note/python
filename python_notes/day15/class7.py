#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Foo:
    def bar(self):
        print("bar")
    # 静态方法 self不是必须的
    @staticmethod  # 装饰器
    def sta():
        print("sta")
    # 类方法
    @classmethod  # 往往不写成self 写成cls
    def class_method(cls):
        print("class method")
# 对象去调用
# obj = Foo()
# obj.bar()
# 传一个对象
# Foo.bar(obj)

# 类直接调用
# Foo.sta()
Foo.class_method()