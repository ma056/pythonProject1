'''
链表组成基础元素就是 节点：因此，需要实现一个节点类的模具。
这个类属性包括：数据域和指针域。
同时还需实现 读取数据域和读取指针域的方法。
还需设置 数据域 和 设置 指针域的方法。
'''


class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None  # 初始指针域为空

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


'''
在有了节点类的基础上，需要创建一个链表类。
属性： 头结点
方法： 增查删节点 以及 链表长度
'''


class lianbiao(object):
    def __init__(self):
        self.head = None  # 头结点指向空

    def add(self, item):  # 增加一个节点
        temp = Node(item)  # 新建一个类节点
        temp.setNext(self.head)  # 让新节点也指向 head 指向 的节点
        self.head = temp  # 令 head 指向当前类节点

    def length(self):  # 统计出节点数量即可
        current = self.head  # 记得保存下头结点
        count = 0
        while current != None:  # 只要头结点为空，则继续循环
            count += 1
            current = current.getNext()
        return count

    def search(self, value):  # 查找链表中是否有这个值，返回一个bool
        current = self.head  # 保存头结点
        while current != None:
            if current.getData() == value:
                return True
            current = current.getNext()
        return None

    def remove(self, value):  # 删除链表中某个节点,
        current = self.head
        previous = None  # 初始值
        found = False
        while not found:  # 只要没找到待删除的值
            if current.getData() == value:
                found = True
            else:
                previous = current  # 若没找到，则向前挪动
                current = current.getNext()
        if previous == None:  # 在找到待删除节点后，若删除的是头结点
            self.head = current.getNext()  # 则直接将头指针指向后一个节点即可
        else:  # 若删除非头结点，则直接指向后一个即可
            previous.setNext(current.getNext())

    def show(self):  # 循环打印链表中元素
        current = self.head
        while current != None:
            value = current.getData()
            current = current.getNext()
            yield value


if __name__ == '__main__':
    mylb = lianbiao()
    mylb.add(9)
    mylb.add(1)
    mylb.add(5)
    mylb.add(4)  # 实例化一个四个节点的链表 [4,5,1,9],链表是倒序存放到！！
    mylb_ele = [ele for ele in mylb.show()]
    print('我的链表中元素为：', mylb_ele)
