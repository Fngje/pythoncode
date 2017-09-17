#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#传递列表
def greet_users(names):
    """向列表中每一位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name + '!'
        print(msg)

usernames = ['hannah','jack','ty','margot']
greet_users(usernames)