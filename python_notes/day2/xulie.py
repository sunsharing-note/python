#! /usr/bin/env python

number = int(input("请输入行数："))

num = 1

while num <= number:
    num1 = 1
    while num1 <= num:
        print("#", end="")
        num1 += 1
    print()
    num += 1