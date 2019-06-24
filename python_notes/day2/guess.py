#! /usr/bin/env python

age = 50


while True:
    user_input_age = int(input("请输入年龄："))
    if user_input_age == age:
        print("yes")
        break
    elif user_input_age > age:
        print("bigger")
    else:
        print("smally")
#        print("太小了")