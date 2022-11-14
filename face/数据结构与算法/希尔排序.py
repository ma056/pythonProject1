#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/8/30 5:21 PM 
@process    :
@change :
'''
'''
一：理解
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
二：待排序[5,8,6,3,9,2,1,7]
第一次（list/2=增量）：5,8,6,3,9,2,1,7   5,9  8,2   6,1    3,7 是一组然后比对组内大小，交换位置后是[5,2,1,3,9,8,6,7]
第二次（第一次的增量/2=增量）：5，1，9，6    2，3，8，7是一组比较大小交换位置后是：[1,25,3,6,7,9,8]
第三次（第二次的增量/2=增量）：1,2，5,3,6,7,9,8  比较大小交换位置后为，1，2，3，5，6，7，8，9
三；代码
    def shell_sort(alist):
        n = len(alist)
        # 初始步长
        gap = int(n / 2)
        while gap > 0:
            # 按步长进行插入排序
            for i in range(gap, n):
                j = i
                # 插入排序
                while j>=gap and alist[j-gap] > alist[j]:
                    alist[j-gap], alist[j] = alist[j], alist[j-gap]
                    j -= gap
            # 得到新的步长
            gap = int(gap / 2)
    
    alist = [54,26,93,17,77,31,44,55,20]
    shell_sort(alist)
    print(alist)
'''


def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = int(n / 2)

    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
        # 得到新的步长
        gap = int(gap / 2)
        print(gap)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
