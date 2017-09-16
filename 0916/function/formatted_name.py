#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()###返回值

musician = get_formatted_name('jimi','hendrix')
print(musician)