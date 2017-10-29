#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

import sys

class MyError(Exception):
    def __str__(self):
        return "I'm a self-defined Error!"

def main():
    try:
        print("************Start of main()************")
        if len(sys.argv) == 1:
            print("python script no parameter.")
            raise MyError()
        print("************End of main()***********")
    except MyError :
        print("Exception happened")

if __name__ == '__main__':
    main()
