"""
设计循环链表

功能：
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node


class SingleCircleLinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0
        else:
            p = self._head
            l = 1
            while p._next != self._head:
                l += 1
                p = p._next
        return l

    def travel(self):
        p = self._head
        while p._next != self._head:
            print(p.data, end=' ')
            p = p._next
        print(p.data, end='\n')

    def add(self, value):
        node = Node(value)
        if self.is_empty():
            self._head = node
            node._next = node
            return
        else:
            p = self._head
            while p._next != self._head:
                p = p._next
            node._next = self._head
            p._next = node
            self._head = node

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self._head = node
            node._next = self._head
            return
        else:
            p = self._head
            while p._next != self._head:
                p = p._next
            p._next = node
            node._next = self._head
            return

    def insert(self, index, value):
        if index <= 0:
            self.add(value)
        elif index >= self.length():
            self.append(value)
        else:
            node = Node(value)
            p = self._head
            position = 0
            while position < index-1:
                p = p._next
                position += 1
            node._next = p._next
            p._next = node

    def remove(self, value):
        if self._head == None:
            return
        p = self._head
        cur = None
        while p._next != self._head:
            if p.data != value:
                cur = p
                p = p._next
            else:
                if p == self._head:
                    p1 = self._head
                    while p1._next != self._head:
                        p1 = p1._next
                    self._head = p._next
                    p1._next = self._head
                else:
                    cur._next = p._next
                return
        if p.data == value:
            if p == self._head:
                self._head = None
            else:
                cur._next = p._next
    
    def search(self, value):
        if self.is_empty():
            return False
        p = self._head
        while p._next != self._head:
            if p.data == value:
                return True
            else:
                p = p._next
        return False

if __name__ == '__main__':
    ll = SingleCircleLinkedList()
    print(ll.is_empty())
    print(ll.length())
 
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
 
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.travel()
    ll.insert(-1,20)
    ll.travel()
    ll.insert(2,30)
    ll.travel()
    ll.insert(10,200)
    ll.travel()
 
    ll.remove(20)
    ll.travel()
    ll.remove(200)
    ll.travel()