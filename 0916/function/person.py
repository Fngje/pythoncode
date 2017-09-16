#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

def build_person(first_name,last_name,age=''):
    '''返回一个字典，包含有关一个人的信息'''
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=22)
print(musician)