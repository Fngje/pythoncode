#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    print("\nMake a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)