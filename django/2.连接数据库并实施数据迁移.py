#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/20 2:27 PM 
@process    :
@change :
'''
# 在配置文件settings.py里配置数据库信息（注意密码要换成自己数据库的密码
# 1.settings中配置连接数据库
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books',
        'USER': 'root',
        'PASSWORD': 'ma123456',
        'HOST': '127.0.0.1',
        'POST': '3306'
    }
}
# 2.设置数据库连接模块
# 在项目的初始化文件里设置数据库连接模块
# 在项目名一样的文件夹下的__init__文件中
# import pymysql
# pymysql.version_info = (1, 4, 13, "final", 0)
# pymysql.install_as_MySQLdb()
# 3.执行数据迁移命令
# 在控制台依次执行两条数据迁移命令，生成数据表
# python manage.py makemigrations   生成迁移文件
# python manage.py migrate
