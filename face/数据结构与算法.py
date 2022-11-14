'''
1、基本的算法有哪些，怎么评价一个算法的好坏?
    基本的算法有: 排序算法(简单排序， 快速排序， 归并排序)， 搜索(二分搜索)， 对于其他基本数 据结构， 栈， 队列，树，都有一些基本的操作。
    评价算法的好坏一般有两种: 时间复杂度和空间复杂度。
    时间复杂度:同样的输入规模(问题规模)花费多少时间。
    空间复杂度:同样的输入规模花费多少空间(主要是内存)。
    以上两点越小越好。
    稳定性:不会引文输入的不同而导致不稳定的情况发生。
    算法的思路是否简单:越简单越容易实现的越好。
2、斐波那契数列
    斐波那契数列:简单地说，起始两项为 0 和 1，此后的项分别为它的前两项之和。
    def fibo(num):
    numList = [0, 1]
    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    return numList


'''
# https://jackkuo666.github.io/Data_Structure_with_Python_book/chapter1/section7.html
# https://blog.csdn.net/QLeelq/article/details/113694455
# https://www.zybuluo.com/listenviolet/note/1399285
#
# li = [54, 26, 93, 17, 77]
# for i in range((len(li) - 1), 0, -1):
#     for j in range(i):
#         print(j, j + 1)
#         print(li[j], li[j + 1])
#         if li[j] > li[j + 1]:
#             li[j], li[j + 1] = li[j + 1], li[j]
# print(li)

# list1 = [5, 1, 4, 8, 2]
# length = len(list1)
# for i in range(length):
#     for j in range(length-i-1):
#         if list1[j] > list1[j + 1]:
#                 list1[j], list1[j + 1] = list1[j + 1], list1[j]
# print(list1)


# list1 = [3, 2, 1, 4, 6, 5]
# length = len(list1)
# for i in range(length):
#     min = i
#     for j in range(i + 1, length):
#         if list1[j] < list1[min]:
#             min = j
#             # list1[min], list1[j] = list1[j], list1[min]
#     list1[min], list1[i] = list1[i], list1[min]
# print(list1)


# list1 = [3, 2, 1, 4, 6, 5]
# length = len(list1)
# for i in range(1, length):
#     j = i  # 表示当前的位置
#     while j > 0 and list1[j] < list1[j - 1]:  # 当前位置可循环，和右边的比左边的小时
#         list1[j - 1], list1[j] = list1[j], list1[j - 1]
#         j -= 1
#
# print(list1)
def fibo(num):
    numList = [0, 1]
    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    print(numList)
    return numList

fibo(3)