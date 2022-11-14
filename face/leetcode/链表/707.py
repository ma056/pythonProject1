#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/16 3:06 PM 
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

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def add_head(self, item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def length(self):
        '''链表的长度'''
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        # print("")

    def get(self, index):
        # i = 0
        # cur = self._head
        # while i <= index:
        #     if i == index:
        #         print(f"index:{cur.item}")
        #     cur = cur.next
        #     i += 1
        cur = self._head
        if 0 <= index < self.length():
            for _ in range(index):
                cur = cur.next
                index -= 1
            print(f"index:{cur.item}")
        else:
            print(f"index:{-1}")

    def append(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add_head(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add_head(1)
    ll.add_head(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.get(4)
    # ll.remove(1)
    print("length:", ll.length())
    ll.travel()
