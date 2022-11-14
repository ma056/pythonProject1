#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/14 10:18 AM 
@process    :
@change :
'''


class SingleNode(object):
    '''链表的节点'''

    def __init__(self, item):
        self.item = item  # 存放数据元素
        self.next = None  # _next是下个节点的标识


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def append(self, item):
        node = SingleNode(item)
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def reverse(self):
        pre = None
        cur = self._head
        while cur != None:
            temp = cur.next
            cur.next = pre  # 这里就是转方向
            pre = cur
            cur = temp
    # def show(self):  # 循环打印链表中元素
    #     current = self._head
    #     while current != None:
    #         value = current.item
    #         current = current.next
    #         yield value


if __name__ == '__main__':
    vall = SingleLinkList()
    vall.append(2)
    vall.append(3)
    vall.append(4)
    # vall.travel()
    vall.reverse()
    # mylb_ele = [ele for ele in vall.show()]
    vall.travel()
