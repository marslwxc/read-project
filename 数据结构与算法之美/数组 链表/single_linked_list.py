"""
设计单链表

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


class SingleLinkedList:
    def __init__(self):
        self._head = None


    def is_empty(self):
        return self._head == None

    def length(self):
        l = 0
        p = self._head
        while p != None:
            l += 1
            p = p._next
        return l

    def travel(self):
        p = self._head
        while p != None:
            print(p.data)
            p = p._next
        print()

    def add(self, value):
        node = Node(value)
        if self._head == None:
            self._head = node
        else:
            node._next = self._head
            self._head = node

    def append(self, value):
        node = Node(value)
        if self._head == None:
            self._head = node
        else:
            p = self._head
            while p._next != None:
                p = p._next
            p._next = node

    def insert(self, index, value):
        if index <= 0:
            self.add(value)
        elif index >= self.length():
            self.append(value)
        else:
            node = Node(value)
            p = self._head
            position = 0
            while position < index:
                position += 1
                p = p._next
            # cur = p._next
            # p._next = node
            # node._next = cur
            node._next = p._next
            p._next = node

    def remove(self, value):
        if self._head == None:
            return 
        p = self._head
        cur = None
        while p != None:
            if p.data != value:
                cur = p
                p = p._next
            else:
                if p == self._head:
                    self._head = p._next
                else:
                    cur._next = p._next
                    break

    def search(self, value):
        p = self._head
        while p != None:
            if p.data != value:
                p = p._next
            else:
                return True
        return False

if __name__ == "__main__":
    single_obj=SingleLinkedList()
    print(single_obj.is_empty())
    print(single_obj.length())
    single_obj.append(1)
    single_obj.append(2)
    single_obj.append(3)
    single_obj.append(4)
    single_obj.append(5)
    single_obj.travel()
    single_obj.add(-1)
    single_obj.travel()
    single_obj.insert(-1,-2)
    single_obj.travel()
    single_obj.insert(2,0)
    single_obj.travel()
    print(single_obj.search(0))
    single_obj.remove(2)
    single_obj.travel()

