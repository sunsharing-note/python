#! /usr/bin/env python
# _*_ coding: utf-8 _*_

age_of_prin = 50
guess_age = int(input("请输入数字:"))

if guess_age == age_of_prin:
    print("yes")
elif guess_age > age_of_prin:
    print("bigger")
else:
    print("small")