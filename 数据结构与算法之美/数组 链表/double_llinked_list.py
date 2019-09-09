"""
双向链表

功能：
is_empty() 链表是否为空
length() 链表长度
travel() 遍历链表
add(item) 链表头部添加
append(item) 链表尾部添加
insert(pos, item) 指定位置添加
remove(item) 删除节点
search(item) 查找节点是否存在
"""
class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self._next = next_node
        self._prev = prev_node

class DoubleLinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        p = self._head
        count = 0
        while p != None:
            count += 1
            p = p._next
        return count

    def travel(self):
        p = self._head
        while p != None:
            print(p.data, end=' ')
            p = p._next
        print()

    def add(self, value):
        node = Node(value)
        if self._head == None:
            self._head = node
        else:
            self._head._prev = node
            node._next = self._head
            self._head = node

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self._head = node
        else:
            p = self._head
            while p._next != None:
                p = p._next
            p._next = node
            node._prev = p

    def insert(self, index, value):
        node = Node(value)
        if self.is_empty():
            self._head = node
        else:
            p = self._head
            position = 0
            while position != index-1:
                position += 1
                p = p._next
            node._next = p._next
            node._prev = p
            node._next.__prev = node
            p._next = node

    def remove(self, value):
        p = self._head
        while p != None:
            if p.data != value:
                p = p._next
            else:
                if p == self._head:
                    self._head = p._next
                    if p._next:
                        p._next._prev = None
                else:
                    p._prev._next = p._next
                    if p._next:
                        p._next._prev = p._prev
                break

    def search(self, value):
        p = self._head
        while p != None:
            if p.data == value:
                return True
            p = p.next
        return False