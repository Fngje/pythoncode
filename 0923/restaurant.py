#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

class Restaurant():
    """创建一个餐厅的类"""

    def __init__(self,name,type):
        """初始化餐厅的属性"""
        self.name = name
        self.type = type

    def descibe_restaurant(self):
        print("The restaurant's name is " + self.name + ".")
        print("The restaurant's type is " + self.type + ".")

    def open_restaurant(self):
        print("The restaurant "+ self.name + " is opening.")

restaurant = Restaurant('come_on','chinese')
restaurant.descibe_restaurant()
restaurant.open_restaurant()

num1_res = Restaurant('num1','chinese')
num2_res = Restaurant('num2','american')
num3_res = Restaurant('num3','japanse')

num1_res.descibe_restaurant()
num2_res.descibe_restaurant()
num3_res.descibe_restaurant()