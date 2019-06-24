#! /usr/bin/env python

num = 1

while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1
'''
else:
    print("hello world")''' #while后面是可以跟else的，当程序正常执行时会执行，如遇到break，则不执行