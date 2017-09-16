#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

def get_formatted_name(first_name,last_name,middle_name=''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + ' ' +middle_name + " " + last_name
        return full_name.title()###返回值
    else:
        full_name = first_name + " " + last_name
        return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('jimi','lee','hendrix')
print(musician)