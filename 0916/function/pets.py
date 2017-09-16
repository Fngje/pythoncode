#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type +"'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
describe_pet('dog','willie')
#####实参的位置很重要

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')
###利用关键字参数传递实参，实参位置可以随意


#######默认值
def describe_pet(pet_name,animal_type='dog'):####默认值必须放在形参后面定义
    '''显示宠物的信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type +"'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')