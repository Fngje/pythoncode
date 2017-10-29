#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

try:
    myList = [4,6]
    print(myList[10])
    print("This is never been called")
except ZeroDivisionError:
    print("ZeroDivisionError happened")
except (IndexError,EOFError):
    print("Exception happened")
except :
    print("Unknown exception happened")
else:
    print("No exception happened")
finally:
    print("Process finished!")