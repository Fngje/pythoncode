#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

# name = input("Please enter your name: ")
# print("Hello " + name + " !")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + " !")

message = "And how old are you？ "
age = int(input(message))

if age <= 18:
    print("So young!")
else:
    print("That's a great age!")