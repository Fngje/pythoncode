#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:jie.fang

#函数存储在模块中，导入整个模块
import pizza_pro
pizza_pro.make_pizza(16,'pepperoni')
pizza_pro.make_pizza(20,'mushrooms','green peppers','extra cheese')


#导入特定的函数
#从哪个模块中导入某个函数
from pizza_pro import make_pizza
make_pizza(16,'pepperoni')
make_pizza(20,'mushrooms','green peppers','extra cheese')

#用as给函数指定别名
from pizza_pro import make_pizza as mp
mp(16,'pepperoni')
mp(20,'mushrooms','green peppers','extra cheese')

#as还可以给模块指定别名
import pizza_pro as mpp
mpp.make_pizza(16,'pepperoni')
mpp.make_pizza(20,'mushrooms','green peppers','extra cheese')

#从模块中导入所有函数
from pizza_pro import *
make_pizza(16,'pepperoni')
make_pizza(20,'mushrooms','green peppers','extra cheese')