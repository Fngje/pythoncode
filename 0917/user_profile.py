#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#使用任意数量保持的关键字参数
def build_profile(first,last,**user_info):#####注意是两个**
    '''创建一个字典，期中包含我们知道有关用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)