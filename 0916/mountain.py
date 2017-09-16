#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

responses = {}

polloing_active = True

while polloing_active:
    name = input("\nWhat is your name？ ")
    response = input("Which mountain would like to climb someday? ")
    responses[name] = response

    repeat = input("Would like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polloing_active = False

print("\n------ Poll Result ------")
for name,responses in responses.items():
    print(name + " would like to climb " + responses + ".")