#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/10/6 1:40 PM 
@process    :
@change :
'''
import time

# promos = []
#
#
# def promotion(f):
#     print('running register(%s)'% f)
#     promos.append(f)
#     return f
#
# @promotion
# def f1():
#     '''积分为1000或以上的客户提供5%折扣'''
#     print('runing 1')
#
# print(promotion)
# f1()

'''
一、为一个函数添加两个装饰器

def how_much_time(func):
    print('how_much_time函数开始了')

    def inner():
        t_start = time.time()
        func()
        t_end = time.time()
        print('一共花费了{0}秒时间'.format(t_end - t_start))

    return inner


def mylog(func):
    print('mylog函数开始了')

    def inner_1():
        print('start')
        func()
        print('end')

    return inner_1


@mylog
@how_much_time
# 相当于mylog(how_much_time(sleep_5s))
# 执行的顺序先how_much_time外部函数-》mylog外部函数->mylog内部函数->how_much_time内部函数
def sleep_5s():
    time.sleep(5)
    print('%d秒结束了' % (5,))


if __name__ == '__main__':
    sleep_5s()
    
'''

'''
二 类装饰器
类装饰器这个写法，主要思路就是返回一个增加了新功能的函数对象，只不过这个函数对象是一个类的实例对象。由于装饰器是可调用对象，所以必须在类里面实现__call__方法，这样由类生成的各种实例加上()就可以运行了
1.不带参数
import time
class Decorator:
    def __init__(self,func):
        self.func = func

    def defer_time(self):
        time.sleep(5)
        print('延时结束')
    def __call__(self,*args,**kwargs):
        self.defer_time()
        self.func()

@Decorator
def f1():
    print('延时之后我才开始执行')

f1()
2.带参数得装饰器
import time
class Decorator:
    def __init__(self,func):
        self.func = func

    def defer_time(self,time_sec):
        time.sleep(5)
        print('{0}延时结束'.format(time_sec))
    def __call__(self,time):
        self.defer_time(time)
        self.func()

@Decorator
def f1():
    print('延时之后我才开始执行')

f1(5)   #5传送到__call__得参数time
'''

'''
无参装饰器
def count_time(func):
    print('开始')
    def inner(x, y):
        t_start = time.time()
        func(x, y)
        t_end = time.time()
        print('一共花费了{0}秒时间'.format(t_end - t_start))
    return inner

@count_time
def index(x, y):
    time.sleep(3)
    print('index %s %s' % (x, y))
    
index(x=1, y=222)
'''


'''
例子:
def login(func):
    print('开始进入装饰器')

    def wrapper(*args, **kwargs):
        name = input('你的账号:').strip()
        pwd = input('你的密码:').strip()
        if name == 'ma' and pwd == '123':
            # func()都执行对了
            res = func(*args, **kwargs)
            return res
        else:
            print('账号密码错误!')
    return wrapper
@login
def index():
    print('欢迎来到主页面')
index()
'''

'''
https://www.cnblogs.com/tobyqin/p/python-decorator.html
1.无参数:
    def debug(func):
        def wrapper():
            print('[DEBUG]:enter: {}'.format(func.__name__))
            return func()
        return wrapper
    
    @debug
    def say_hello():
        print('hello')
    
    say_hello()
2.函数有参数:
    def debug(func):
        def wrapper(something):
            print('[DEBUG]:enter: {}'.format(func.__name__))
            return func(something)
        return wrapper
    
    @debug
    def say_hello(somthing):
        print('hello--{}'.format(somthing))
    
    say_hello('111')
3.函数有参数通用:
    def debug(func):
        def wrapper(*args,**kwargs):
            print('[DEBUG]:enter: {}'.format(func.__name__))
            return func(*args,**kwargs)
        return wrapper
    
    @debug
    def say_hello(something):
        print('hello--{}'.format(something))
    
    say_hello('111')

4.带参数的装饰器:
    def logging(level):
        def wrapper(func):
            def inner_wrapper(*args,**kwargs):
                print('[{level}]:enter: function{func}'.format(level=level,func = func.__name__))
                return func(*args,**kwargs)
            return inner_wrapper
        return wrapper
    
    @logging(level='info')
    def say(something):
        print('say {}!'.format(something))
    
    @logging(level='debug')
    def do(something):
        print('do {}...'.format(something))
    
    if __name__ == '__main__':
        say('hello')
        do('my work')

5.基于类的装饰器
    class logging(object):
        def __init__(self,func):
            self.func = func
        def __call__(self, *args, **kwargs):
            print('[DEBUG]:enter function {func}'.format(func=self.func.__name__))
            return self.func(*args,**kwargs)
    
    @logging
    def say(something):
        print('sqy {}!'.format(something))
    if __name__ == '__main__':
        say('hello')
6.带参数类装饰器:
    class logging(object):
        def __init__(self,level = 'info'):
            # self.func = func
            self.level = level
        def __call__(self,func):
            def wrapper(*args,**kwargs):
                print('[{level}]:enter: function{func}'.format(level=self.level, func=func.__name__))
                func(*args,**kwargs)
            return wrapper
    
    
    @logging(level = 'info')
    def say(something):
        print('sqy {}!'.format(something))
        
    if __name__ == '__main__':
        say('hello')
'''


def html_tags(tag_name):
    print('begin outer function.')
    def wrapper_(func):
        print("begin of inner wrapper function.")
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            print("<{tag}>{content}</{tag}>".format(tag=tag_name, content=content))
        print('end of inner wrapper function.')
        return wrapper
    print('end of outer function')
    return wrapper_

@html_tags('b')
def hello(name='Toby'):
    return 'Hello {}!'.format(name)
hello()
hello()