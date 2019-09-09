"""
Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
size() 返回栈中的 item 数量。不需要参数，并返回一个整数。
"""
class ListNode:
    def __init__(self, value, next_node=None):
        self.data = value
        self._next = next_node


class Stack:
    def __init__(self):
        self._head = None

    def push(self, value):
        node = ListNode(value)
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur._next != None:
                cur = cur._next
            cur._next = node

    def pop(self):
        if self._head == None:
            return False
        else:
            cur = self._head
            prev = None
            while cur._next != None:
                prev = cur
                cur = cur._next
            prev._next = None
            return cur.data
            

    def peek(self):
        cur = self._head
        while cur._next != None:
            cur = cur._next
        return cur.data

    def isEmpty(self):
        return self._head == None

    def size(self):
        cur = self._head
        count = 0
        while cur != None:
            cur = cur._next
            count += 1
        return count

if __name__ == "__main__":
    s=Stack()

    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())     