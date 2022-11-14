#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/27 3:53 PM 
@process    :
@change :
'''
import os

'''
os模块的主要功能：系统相关、目录及文件操作、执行命令和管理进程
1.系统相关的
    os.name->查看当前操作系统的名称，windows返回nt,mac,linux返回的是posix
    os.environ->获取系统的环境变量
    os.sep->当前平台的分隔符，'/'
    os.altsep->可替代的路径分隔符 mac：none
    os.extsep->文件名和文件扩展名之间分隔的符号，在Windows下为‘.’。
    os.pathsep->PATH环境变量中的分隔符，在POSIX系统中为‘:’，在Windows中为‘;’。
    ...
  
2.文件和目录操作
    os.getcwd()->获取当前工作目录，即当前python脚本工作的目录路径
    os.chdir("dirname")->改变当前脚本工作目录；相当于shell下cd
    os.curdir->返回当前目录: ('.')
    os.makedirs('dir1/dir2',exsit=Flase) 生成文件夹
    os.removedirs(‘dirname1’)->递归删除空目录（要小心）
    os.mkdir('dirname')->生成单级目录
    os.listdir('dirname')->列出指定目录下的所有文件和子目录，包括隐藏文件
    os.remove('filename')->删除一个文件
    os.rename("oldname","new")->重命名文件/目录
    os.path.split(path)->将path分割成目录和文件名二元组返回(path,name) = os.path.split(path)
    os.path.dirname(path) ->返回目录
    os.path.basename(path)->返回文件名
    os.path.exists(path或者file)->如果path存在，返回True；如果path不存在，返回False
    os.path.join(path1[, path2[, ...]])->将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
    os.path.getsize(filename)->返回文件包含的字符数量
    
3.os.walk(top, topdown=True, onerror=None, followlinks=False) 
->walk方法是os模块中非常重要和强大的一个方法。可以帮助我们非常便捷地以递归方式自顶向下或者自底向上的方式遍历目录树，
对每一个目录都返回一个三元元组(dirpath, dirnames, filenames)。
    for root, dirs, files in os.walk(r"c:\python36"):
        print("\033[1;31m-"*8, "directory", "<%s>\033[0m" % root, "-"*10)
        for directory in dirs:
            print("\033[1;34m<DIR>    %s\033[0m" % directory)
        for file in files:
            print("\t\t%s" % file)
4.os.popen(command, [mode, [bufsize]])->popen也可以运行操作系统命令，并通过read()方法将命令的结果返回，不像system只能看不能存，这个能存！
    >>> os.popen('ipconfig')
    <os._wrap_close object at 0x0000000002BB8EF0>
    >>> ret = os.popen('ipconfig')
    >>> ret.read()
    '\nWindows IP 配置\n\n\n以太网适配器 Bluetooth 网络连接 2:\n\n   媒体状态  . . . . . . . . . . . . : 媒体已断开\n   连接特定的 DNS 后缀 . . . . . . . : \n\n无线局域网适配器 无线网络连接 2:\n\n   媒体状态  . . . . . . . . . . . . : 媒体已断开\n   连接特定的 DNS 后缀 . . . . . . . : \n\n无线局域网适配器 无线网络连接:\n\n   连接特定的 DNS 后缀......

'''
'''
os.path和pathlib对比
import os
from pathlib import Path
1.获取当前文件路径
path1 = os.getcwd()
path2 = Path.cwd()
2.获取上层、上上层目录
print(os.path.dirname(path1))
print(path2.parent)
3.拼接目录
print(os.path.join(path1,'img.jpg'))
print(os.path.join(path1,'path','img.jpg'))

print(path2.join('img.jpg'))
print(os.path.join(path1,'path','img.jpg'))
4.创建文件夹并重命名
os.makedirs(os.path.join('path','test'),exist_ok = True)
os.rename('test.txt',os.path.join('path','tests.txt'))

Path('path/test').mkdir(parents=True,exist_ok = True)
Path('test.txt').rename('path/test.txt')
'''
