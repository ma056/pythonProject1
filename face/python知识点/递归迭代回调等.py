# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 递归迭代回调等.py
@Author : wenjing
@Date : 2022/12/13 10:03
"""


# 递归和回调函数区别:
#     回调函数是在一个函数中“回调函数”以参数的形式传入，并在该函数内部被调用。
#     而递归函数是在一个函数中，调用了自己。
# 函数内部定义函数：闭包
# 函数内部调用其他函数：函数调用
# 函数内部调用参数传过来的函数：回调函数
# 函数内部调用自己这个函数：递归
# 回调：add函数就被称为calculator的回调函数
def calculator(v1, v2, fn):
    result = fn(v1, v2)
    return result


def add(v1, v2):
    return v1 + v2  # 调用calculator，计算1+1 print(calculator(1,1,add))


# 高阶函数Python 也支持高阶函数的概念。如果函数包含其他函数作为参数或返回函数作为输出，则称为高阶函数（Higher Order Function），
# 即与另一函数一起操作的函数称为高阶函数。值得知道的是，这个高阶函数也适用于将函数作为参数或返回函数作为结果的函数和方法。
# Python 中常用的高阶函数有 map() 、reduce() 、filter() 、sorted() 等。
# calculator是高阶函数，而add是回调函数。
def calculator(v1, v2, fn):
    result = fn(v1, v2)
    return result


def add(v1, v2):
    return v1 + v2


# 递归：一个过程或函数在其定义或说明中有直接或间接调用自身的
# 将 10不断除以2，直至商为0，输出这个过程中每次得到的商的值。
def recursion(n):
    v = n // 2  # 地板除，保留整数
    print(v)  # 每次求商，输出商的值
    if v == 0:
        ''' 当商为0时，停止，返回Done'''
        return 'Done'
    v = recursion(v)  # 递归调用，函数内自己调用自己


recursion(10)  # 函数调用
# 迭代

# 生成器
# 迭代器
