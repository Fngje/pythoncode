#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#用python解决斐波那契数列问题
import time

def fbis(num):
    result = [0,1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

def main():
    result = fbis(30)
    fobj = open("D:\\JetBrains\\WorkPlace\\Python3\\高效开发\\result.txt","w+")
    for i,num in enumerate(result):#enumerate生成带索引的迭代序列
        print("第%s个数是： %s"%(i,num))
        fobj.write("%s\n"%num)
        time.sleep(0.5)
    fobj.close()

if __name__ == "__main__":
    main()