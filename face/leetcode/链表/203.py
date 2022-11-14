#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/14 10:18 AM 
@process    :
@change :
'''

# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 输入：head = [], val = 1
# 输出：[]
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
# Definition for singly-linked list.

# def removeElements():
#     head = [1, 2, 6, 3, 4, 5, 6]
#     val = 6
#     dummy_head = ListNode(next=head)  # 添加一个虚拟节点
#     cur = dummy_head
#     while (cur.next != None):
#         if (cur.next.val == val):  #cur.next这个相当于索引，。val取的是植
#             cur.next = cur.next.next  # 删除cur.next节点
#         else:
#             cur = cur.next
#     print(dummy_head.next)
#
# removeElements()


from lianbiao import lianbiao, Node


class DeleteNode(lianbiao):
    def __init__(self):
        super(DeleteNode, self).__init__()  # 链接父类初始化

    # 双指针法
    def deleteNode(self, value):  # 想删除值为value的节点
        previous = None
        current = self.head
        found = False
        while not found:
            if current.getData() != value:
                previous = current
                current = current.getNext()
            else:
                found = True
        if previous == None:  # 若找到后 previous == None,说明删除是头结点
            self.head = current.getNext()  # 则直接令头结点指向后一个节点即可
        else:
            previous.setNext(current.getNext())  # 令前一个节点指向后一个节点即可


if __name__ == '__main__':
    mylb = DeleteNode()
    mylb.add(9)
    mylb.add(1)
    mylb.add(5)
    mylb.add(4)

    mylb.deleteNode(4)
    mylb_ele = [ele for ele in mylb.show()]
    print('我的链表中元素为：', mylb_ele)
