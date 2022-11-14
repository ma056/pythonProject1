#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/26 10:19 AM 
@process    :
@change :
Numpy数组类的名字叫做ndarray，经常简称为array。要注意将numpy.array与标准Python库中的array.array区分开，后者只处理一维数组，并且功能简单。
'''
import numpy as np

# 1. ndarray n维数组  便捷的算术功能和灵活的广播功能
a = np.arange(100)
# print(a)
# rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
a1 = np.random.rand(2, 3)
# print(a1)
# 返回一个或一组样本，具有标准的正态分布
a2 = np.random.randn(2, 3)

# 2.np.array
arr = np.array([1, 2, 3])
# print(type(arr))  # <class 'numpy.ndarray'>
# print(arr.shape)  # (3,)
# print(arr.ndim)  # 1    ndim是数组的轴（维度）的个数
arr2 = np.arange(24)
# print (arr2.ndim)             # a 现只有一个维度
# 现在调整其大小
b = arr2.reshape(2, 4, 3)  # b 现在拥有三个维度

arr3 = np.random.rand(3, 5, 2)  # (3, 5)二维数组三个数组五个元素  (3, 5,2)三维数组三个二维数组，五个三位数组，两个元素
# print(arr3)
# print(arr3.shape)  # (3, 5, 2)
# print(arr3.ndim)  # 3

# 3. 创建制定类型的数组
arr4 = np.array([1, 2, 3], dtype="float32")  # int类型：分有符号和无符号 int8 uint8
# print(arr4.dtype)

# 4.创建数组
x = np.empty([3, 2], dtype=int)  # 并不安全，有时会返回初始化的垃圾数组
x1 = np.zeros((2, 2), dtype=int)
x2 = np.ones((2, 3), dtype=int)
# print(x2)

# 5.算术和广播->广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。
k = np.random.rand(2, 3)
# print(k)
k1 = k + k
# print(k1)
k2 = k * 10
# print(k2)
k3 = k != 1
# print(k3)
# ....

# 6.格式转换
t = np.array([0, 0, 0], dtype='uint8')
t[0] = 100
# print(t)
tt = [1, 2, 999, 127]
tt1 = np.asarray(tt, dtype='int8')
# print(tt1)
tt2 = np.asarray(tt, dtype='uint8')
# print(tt2)
ttt = np.array([2, 3, 4])
tttt = [2, 3, 4]
# print(ttt == tttt)
ttt1 = ttt.astype('string_')  # [b'2' b'3' b'4']
# print(ttt1)
ttt2 = arr.astype('unicode_')  # array(['2', '3', '4'], dtype='<U21')

# 7.切片
# 7.1一维切片
arr_id = np.arange(10)
# print(arr_id[3:6])  # [3 4 5]

# 赋值可以是标量或者ndarrary 不能是list
arr_id[6:] = 8  # [0 1 2 3 4 5 8 8 8 8]
arr_id[2:] = np.arange(8)  # array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
# arr_id[2:] = [0, 1, 7, 8, 8, 8, 7, 8, 8, 8]  # 报错 vauleerror
arr_copy2 = arr_id[2:].copy()

#  7.2二维切片
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(arr_2d[0])  # [1 2 3]
# print(arr_2d[0][1])  # 2
# print(arr_2d[0, 1])  # 2

# 7.3三维切片
arr_3d = np.random.randn(3, 4, 2)
# print(arr_3d[0])
arr_3d[0, 1:]  # 第0个，从第一个元素直到最后

# 8.索引--布尔索引
arr_2d1 = np.random.randn(3, 4)
# print(arr_2d1)
bool_x = np.array([True, False, True])
bool_names = np.array(['jack', 'henry', 'jason'])
arr_2d1[bool_x]  # 用bool选取0,2
# print(arr_2d1[bool_x])  #[True,False,True]第一lie和第三列要，二不要
arr_2d1[bool_names == 'jack']  # 选取第一行 array([[ 1.3291973 ,  0.52318965, -0.49999786, -0.95954392]])
# print(arr_2d1[bool_names == 'jack'])  # ['jack','henry','jason']类似为：为一列加了列名
# arr_2d[(bool_names == 'jack') | (bool_names == 'henry'), 2:]

#  8.1神奇索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
# print(arr)
arr[[2, 1, 7]]  # 注意是两个括号 上面使用布尔值 这边使用index

# 9 reshape 和转轴
# arr.shape # (a,b)
arr = np.arange(32).reshape(8, 4)  # 返回新的
# print(arr.T)  # 返回新的将字数组的数量转为最里面的元素个数，原来的元素个数变为子数组的数量
# arr.reshape(m,-1) #改变维度为m行、d列 （-1表示列数自动计算，d= a*b /m ）
# arr.reshape(-1,m) #改变维度为d行、m列 （-1表示行数自动计算，d= a*b /m ）
arr2 = np.arange(32).reshape(-1, 4)  # 缺省 4*8
arr3 = np.arange(32).reshape(-1, 2, 8)  # 最外层让系统来计算


# 通用函数
# 一元函数
arrr = np.arange(10).reshape(-1, 5)
np.sqrt(arrr)   # 平方根
np.square(arr)  # 平方
np.ceil(arrr)  # 计算每个元素的最高整数值 array([[0., 1., 2., 3., 4.],[5., 6., 7., 8., 9.]])
np.floor(arrr)  # 计算每个元素的最小整数值 array([[0., 1., 2., 3., 4.],[5., 6., 7., 8., 9.]])
np.isnan(arrr)   # 判断每个元素是否为NaN，返回布尔值
np.rint(arrr)  # 保留整数部分 保持dtype 保留到整数位
# 二元函数
np.add(arrr, arrr)  # 将数组的对应元素相加
np.subtract(arrr, arrr)  # 在第二个数组中，将第一个数组中包含的元素去除


# 数字统计
arrr1 = np.random.randn(5, 4)
arrr1.mean()  # 等同np.mean(arr)
arr.mean(axis=0)  # 沿0轴计算，也就是就算每列
arrr1.sum()

# 添加删除去重
# append:将值添加到数组末尾
# insert: 沿指定轴将值插入到指定下标之前
# delete: 返回删掉某个轴的子数组的新数组
# unique: 寻找数组内的唯一元素类似去重
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.append(a, [7, 8, 9]))  # [1 2 3 4 5 6 7 8 9]
print(a)    # [[1 2 3] [4 5 6]]
print(np.insert(a, 3, [11, 12]))  # 在3号位置前插入，变成一维了
print(np.insert(a, 1, [11], axis=0))  # array([[ 1,  2],[11, 11],[ 3,  4],[ 5,  6]])
print(np.delete(a, 5))  # 删除指定位置的元素后，变成一维了
print(np.delete(a, 1, axis=0))      # array([[ 0,  1,  2,  3],[ 8,  9, 10, 11]])
a1 = np.array([0, 1, 4, 7, 2, 1, 4, 3])
print(np.unique(a1))    # array([0, 1, 2, 3, 4, 7])


