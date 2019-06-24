#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


# 在里面定义一个__str__方法 用于在调用时返回值 而不是内存地址
class Author(models.Model):
    name = models.CharField(max_length = 64)
    
    def __str__(self):
        return self.name
