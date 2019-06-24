#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

import configparser

config = configparser.ConfigParser()

# config["DEFAULT"] = {"ServerAliveInterval": 45,
#                      "Compression": "yes",
#                      "CompressionLevel": "9"}
# config["bitbucket.org"] = {}
# config["bitbucket.org"]["User"] = "hg"

# config["topsecret.server.com"] = {}
# #config["topsecret.server.com"][]
# topsecret = config["topsecret.server.com"]
# topsecret["Host Port"] = "50022"

# with open("test.ini", "w") as configfile:
#     config.write(configfile)

config.read("test.ini")
# print(config.sections()) # 默认的这样子是不会显示的
# # print(config.defaults()) # 显示默认的
# # for key in config:
# #     print(key)
# # for key1 in config["bitbucket.org"]: #打印其他的 default的会跟着出来
# #     print(key1)
#print(config["DEFAULT"])
#config.remove_section("topsecret.server.com")
#config.write(open("config.ini","w")) # 如果这里还是写test.ini 则是覆盖 并不是写入
#print(config.has_section("topsecret.server.com"))
#config.set("topsecret.server.com","host port","8080")
#config.write(open("config.ini","w"))
config.set("bitbucket.org", "user","huahua")
config.write(open("config.ini","w"))