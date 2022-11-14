#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/13 11:27 AM 
@process    :
@change :
'''
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 输入: nums = [0]
# 输出: [0]
nums = [0, 1, 0, 3, 12]
# for i, item in enumerate(nums):
#     if item == 0:
#         new_nums = nums.pop(i)
#         nums.insert(len(nums), new_nums)
#         print(nums)
#     else:
#         pass
# print(nums)
left = 0
for i in range(len(nums)):
    if nums[i]:
        print(nums[i], left, i, nums)
        nums[left], nums[i] = nums[i], nums[left]
        left += 1
        print(nums)

# print(nums)
