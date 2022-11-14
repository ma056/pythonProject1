#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/7 4:03 PM 
@process    :
@change :
'''

nums = [1, 1, 1, 1, 0, 1, 1, 1]
c = 0
res = 0
for i in nums:
    if i == 1:
        c += 1
        res = max(res, c)
        print(res)
    else:
        c = 0
print(res)
