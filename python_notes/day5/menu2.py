#! /usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   menu2.py
@Time    :   2018/12/18 21:04:12
@Author  :   chow 
@Version :   1.0
@Contact :   test@app.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
menu = {
    "北京市": {
        "海淀": {
            "海淀一":{
                "海淀一一":{},
                "海淀一二":{},
            },
            "海淀二":{
                "海淀二一":{},
                "海淀二二":{}, 
            },
        },
        "朝阳": {
            "朝阳一":{
                "朝阳一一":{},
                "朝阳一二":{},
            },
            "朝阳二":{
                "朝阳二一":{},
                "朝阳二二":{},
            },
        },
    },
    "重庆市":{
        "渝北区":{
            "渝北一":{
                "渝北一一":{},
                "渝北一二":{},
            },
            "渝北二":{
                "渝北二一":{},
                "渝北二二":{},
            },

        },
        "江北区":{
            "江北一":{
                "江北一一":{},
                "江北一二":{},
            },
            "江北二":{
                "江北二一":{},
                "江北二二":{},
            },
        },
    },
}

current_layer = menu
parent_layers = []
#parent_layer = menu
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>>>:")
    if len(choice) == 0:
        continue
    if choice in current_layer:
        #parent_layer = current_layer
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == "b":
#        current_layer = parent_layer
        if parent_layers:
            current_layer = parent_layers.pop()
    elif choice == "q":
        exit("退出")
    else:
        print("没有这个")