#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/10/8 11:47 AM 
@process    :
@change :
'''
'''
1.安装Django库->pip3 install django==3.0.4
2.创建项目->django-admin startproject mysite(项目名)
    一个新建立的项目结构大概如下：
    mysite/
    manage.py       #程序执行的入口
    mysite/
        __init__.py
        settings.py  #项目的配置文件，数据库，中间件，app
        urls.py         #路由文件，所有的任务都是从这里开始分配，相当于Django驱动站点的目录
        asgi.py
        wsgi.py
3.创建应用->python manage.py startapp artcle

'''