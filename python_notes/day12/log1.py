#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger()
# 写入到日志文件
fh = logging.FileHandler("test.log")
# 输出到屏幕
ch = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)
logger.debug("logger debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")