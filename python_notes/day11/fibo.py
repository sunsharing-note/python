#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib


def fib(max):
    n, before, after = 0, 0, 1

    while n < max:
        yield before
        before, after = after, before + after
        n += 1

print(fib(8))
print(next(fib(8)))