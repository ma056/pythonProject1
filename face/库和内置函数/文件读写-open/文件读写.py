#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/27 3:13 PM 
@process    :
@change :
'''
# 1. f.read(size) ->输出所有类型为str
f = open('../1.txt', 'r')
print(f.read())
f.close()

# 2. f.readline()   ->输出第一行类型为str
f1 = open('../1.txt', 'r')
print(f1.readline())
f1.close()

# 3. f.readlines()  ->输出所有，一行一行按顺序读入list
f2 = open('../1.txt', 'r')
print(f2.readlines())
f2.close()

# write
a = ["11111", '2222']
f3 = open("../foo.txt", "w")
for i in a:
    f3.write(i + '\n')
f3.close()

# with关键字->with关键字用于Python的上下文管理器机制。
# 为了防止诸如open这一类文件打开方法在操作过程出现异常或错误，或者最后忘了执行close方法，文件非正常关闭等可能导致文件泄露、破坏的问题。
# Python提供了with这个上下文管理器机制，保证文件会被正常关闭。在它的管理下，不需要再写close语句。
with open('../11.txt', 'w') as f:
    f.write('Hello, world!')
# 支持打开多个
# with open('log1') as obj1, open('log2', 'w') as obj2:
#     s = obj1.read()
#     obj2.write(s)

a = []
with open('../1111.txt', 'r') as ffff:
    for i, line in enumerate(ffff, 1):
        if 'node170' in line:
            line = line.replace(',node170','')
        elif '172.16.30.170' in line:
            line = line.replace(',172.16.30.170','')
        a.append(line)
print(a)
    # aa = ffff.readlines()
    # for item in aa:
    #
    #     aa.append()
    # print(aa)