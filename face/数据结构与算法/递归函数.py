#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/8/31 2:16 PM 
@process    :
@change :
'''
'''
https://www.cnblogs.com/dosboy/p/python_l1.html
https://cloud.tencent.com/developer/article/1947071

例题：
    f(n) = (f(n-1) + 1)*2 ，告诉你f(1)=1，问f(10)是多少？
    我们直接把这个f(n)定义成函数，并且计算f(10) 如下：
    
    def f(n):
    if n==1:
        return 1
    else:
        return (f(n-1)+1)*2
    print(f(10))
    
例题：猴子第1天摘了一堆桃子吃了一半又多一个，第2天吃了剩下的一半又多一个，...，第10天早上时发现只有1个桃子了。问第1天摘了多少？这回我们把n设为第n天（而不是前n天）
    假设 x2是当天桃子的数量，x1是前一天桃子的数量  x2 = (x1/2)-1   得x1 = (x2+1)*2
    提示：g(n-1) = (g(n)+1) * 2    => g(n) = (g(n+1)+1) * 2 
    def g(n):
    if n==10:
        return 1
    else:
        return 2*(g(n+1)+1)

    print(g(1))
    
    

'''
