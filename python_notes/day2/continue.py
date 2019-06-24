#! /usr/bin/env python

num = 1

while num <= 10:
    num += 1
    if num == 3:
        continue #break
    print(num)
'''
else:
    print("hello world")''' #while后面是可以跟else的，当程序正常执行时会执行，如遇到break，则不执行