#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

class User():
    """定义一个user类"""

    def __init__(self,first_name,last_name,age,sex,salary,height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.height = height

    def describe_user(self):
        print("Basic Info:\nFirst name: " + self.first_name.title() + "\nLast name: " + self.last_name.title() + "\nAge: " + str(self.age) + "\nSex: " + self.sex.title() + "\n")

    def greet_user(self):
        print("Welcome " + self.first_name.title() + "." + self.last_name.title() + " !")

jie = User('jie','fang',24,'man',8000,175)
jie.describe_user()
jie.greet_user()