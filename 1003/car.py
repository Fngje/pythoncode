#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

class Car():
    """一次模拟汽车的尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        '''将里程表数值设为一个指定的值，并且数值不能回调'''
        if mileage >= self.odometer_reading:
            self.odometer_reading =mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表数值增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("The miles can't be less than 0!")

my_new_car =Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

#直接修改属性的值
my_new_car.odometer_reading = 30
my_new_car.read_odometer()
#通过方法修改属性的值
my_new_car.update_odometer(34)
my_new_car.read_odometer()

my_used_car = Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(-100)
my_used_car.read_odometer()


