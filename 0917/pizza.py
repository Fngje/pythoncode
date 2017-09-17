#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#向函数传递任意数量的实参
def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print("\nMake a pizza with the following toppings: ")
    for topping in toppings:
        print("_ " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')