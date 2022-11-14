#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/10/9 10:26 AM 
@process    :
@change :
'''
# a = [1, 2, 3, 4]
# aa = [lambda x: x * 2 for x in a]
# print(aa)
# a1=[(lambda x:x*x)(x) for x in range(5)]
#
# print(a1)
# aaaa = {e:3 for e in a}
# print(aaaa)
# b = lambda: {x: 3 for x in a}
# print(b)
a = [1, 2, 3, 4, 5]
# list1 = [lambda x: x + i for i in range(5)]
# for list2 in list1:
#     print(list2(5))
# print('-----------')
#
# list1 = [lambda: i for i in range(5)]
# for list2 in list1:
#     print(list2())

# list1 = [lambda: i for i in a]
# for list2 in list1:
#     print(list2())
# list1 = [lambda i: i for i in a]
# print(list1[0])
# # for list2 in list1:
# #     print(list2(1))


list1 = [lambda x: x + i for i in range(5)]
for list2 in list1:
    print(list2(5))
print('-----------')


def fun1(x):
    return x + i


lst = []


def fun():
    for i in range(5):
        lst.append(i)
    return lst


lst = []
def fun():
    for i in range(5):
        def fun1(x):
            return x + i

        lst.append(fun1)
    return lst
r = fun()
print(r)
