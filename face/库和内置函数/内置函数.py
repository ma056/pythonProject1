#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/27 2:10 PM 
@process    :
@change :
'''

'''
数据格式转换：
    int()、float()、list()、dict()、set()、tuple()
max()/min()/sum()/len():
    返回给定集合里的最大或者最小的元素。可以指定排序的方法
    sum()传入一个可迭代对象sum([1,2,3])
sorted()
    sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
枚举函数->enumerate()     #(dic, 1)表示从1开始，没有的时候是默认从0开始
    dic = {
    "k1":"v1",
    "k2":"v2",
    "k3":"v3",
    }   
    for i, key in enumerate(dic, 1):    
        print(i,"\t",key)
eval()
    将字符串直接解读并执行,
    例如：s = "6*8"，s是一个字符串，d = eval(s)， d的结果是48。
format()
    1.填充字符串
    1.1.通过位置来填充字符串
        eg：print('hello {0} i am {1}'.format('world','python'))    # 输入结果：hello world i am python
    2.数字格式化
        print("{:.2f}".format(3.1415926))
    3.格式化datetime
        from datetime import datetime
        now=datetime.now()
        print '{:%Y-%m-%d %X}'.format(now) # 输出结果：2017-07-24 16:51:42
frozenset()
    返回一个不能增加和修改的集合类型对象和set的区别就是set可以增加和修改
id()
    返回对象的内存地址,常用来查看变量引用的变化，对象是否相同等。常用功能之一！
isinstance()
    判断一个对象是否是某个类的实例。比type()方法适用面更广。
    >>> isinstance("haha", str)
    True
    >>> isinstance(1, str)
    False
filter()
    过滤器，用法和map类似。在函数中设定过滤的条件，逐一循环对象中的元素，将返回值为True时的元素留下（注意，不是留下返回值！），形成一个filter类型的迭代器。
    def f1(x):
    if x > 3:
        return True
    else:
        return False
    li = [1,2,3,4,5]
    data = filter(f1,li)
    print(type(data))
    print(list(data))
map()
    map() 会根据提供的函数对指定序列做映射。
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    def square(x) :         # 计算平方数
         return x ** 2
    map(square, [1,2,3,4,5])    # 计算列表各个元素的平方
    <map object at 0x100d3d550>     # 返回迭代器
    list(map(square, [1,2,3,4,5])) 
'''