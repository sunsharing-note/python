#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# here put the import lib

# log有5个级别 依次为 critical>error>warning>info>debug>notset
# warning为默认级别
import logging


# 默认打印在屏幕上
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%a,%d %b %Y %H:%M:%S",
                    filename="test.log",
                    filemode="a")
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")