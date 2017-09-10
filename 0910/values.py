#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang


for i in range(0,11):
    print(i)

#利用list和range创建一个数字列表
numbers = list(range(0,11))
print(numbers)

#range还可以指定步长
numbers = list(range(2,11,2))#10以内的所有偶数
print(numbers)

squares = []
for i in range(0,11):
    # square = i**2
    # squares.append(square)
    squares.append(i**2)
print(squares)

print(min(squares))
print(max(squares))
print(len(squares))
print(sum(squares))