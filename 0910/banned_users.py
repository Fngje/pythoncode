#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post response if you wish.")