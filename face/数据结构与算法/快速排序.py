#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/8/30 1:55 PM 
@process    :
@change :
'''
'''
https://cloud.tencent.com/developer/article/1794176
一：快速排序(Quick Sort)是一种效率很高的排序算法，是对冒泡排序的一种改进排序算法。
快速排序首先任意选取一个数据(通常选待排序列表中的第一个数)作为基准数据，将待排序列表中的数据分割成独立的两部分，所有比基准数据小的数都放到它左边，
所有比基准数据大的数都放到它右边，此时基准数据排序完成，第一轮快速排序完成。然后再按此方法对两部分的数据分别进行快速排序，
整个排序过程可以递归进行，直到被分割的数据只有一个或零个时，递归结束，列表排序完成。

二：原理
1. 从待排序列表中选取一个基准数据(通常选取第一个数据)。
2. 将待排序列表中所有比基准数据小的元素都放到基准数据左边，所有比基准数据大的元素都放到基准数据右边(升序排列，降序反之)。
    用基准数据进行分割操作后，基准数据的位置就是它最终排序完成的位置，第一轮排序完成。
3. 递归地对左右两个部分的数据进行快速排序。即在每个子列表中，选取基准，分割数据。直到被分割的数据只有一个或零个时，列表排序完成。

三：代码
    def quick_sort(array, start, end):
        if start >= end:
            return
        mid_data, left, right = array[start], start, end
        while left < right:
            while array[right] >= mid_data and left < right:
                right -= 1
            array[left] = array[right]
            while array[left] < mid_data and left < right:
                left += 1
            array[right] = array[left]
        array[left] = mid_data
        quick_sort(array, start, left-1)
        quick_sort(array, left+1, end)
    
    
    if __name__ == '__main__':
        array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
        quick_sort(array, 0, len(array)-1)
        print(array)
'''


def quick_sort(array, start, end):
    # 递归的退出条件
    if start >= end:
        return
    mid_data, left, right = array[start], start, end
    while left < right:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while array[right] >= mid_data and left < right:
            right -= 1
        # 将right指向的元素放到left的位置上
        array[left] = array[right]
        # 如果left与right未重合，left指向的元素比基准元素小，则low向右移动
        while array[left] < mid_data and left < right:
            left += 1
        # 将low指向的元素放到high的位置上
        array[right] = array[left]
        # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
        # 将基准元素放到该位置
    array[left] = mid_data
    # 对基准元素左边的子序列进行快速排序
    quick_sort(array, start, left - 1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(array, left + 1, end)


if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    quick_sort(array, 0, len(array) - 1)
    print(array)
