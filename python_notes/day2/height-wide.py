#! /usr/bin/env python

height = int(input("请输入高："))
width = int(input("请输入宽："))

num1 = 1
while num1 <= height:
    num2 = 1
    while num2 <= width:
        print("#", end="")
        num2 += 1
    print()
    num1 += 1