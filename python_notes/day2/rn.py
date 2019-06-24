#! /usr/bin/env python

num1 = 0
#num2 = 0

while num1 <= 5:
    print(num1,end="_")
    num2 = 0
    while num2 <= 7:
        print(num2,end="_")
        num2 += 1
    num1 += 1
    print() # 等价于 print(end="\n")