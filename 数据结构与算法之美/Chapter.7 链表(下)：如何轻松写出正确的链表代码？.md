
# 技巧1：理解指针或引用的含义

**将某个变量赋值给指针，实际上就是将这个变量的地址赋值给指针，或者反过来说，指针中存储了这个变量的内存地址，指向了这个变量，通过指针就能找到这个变量。**

# 技巧2：警惕指针丢失和内存泄漏

在插入和删除结点时，一定要注意操作的顺序，防止指针丢失使链表断开，造成内存泄露

不知道你有没有这样的感觉，写链表代码的时候，指针指来指去，一会儿就不知道指到哪里了。所以，我们在写的时候，一定注意不要弄丢了指针。+指针往往都是怎么弄丢的呢？我拿单链表的插入操作为例来给你分析一下

![删除链表结点](https://img2018.cnblogs.com/blog/1256425/201810/1256425-20181005114852493-254453134.png)

如图所示，我们希望在结点 a 和相邻的结点 b 之间插入结点 x，假设当前指针 p 指向结点 a。如果我们将代码实现变成下面这个样子，就会发生指针丢失和内存泄露。
```python
p.next = x
x.next = p.next
```
初学者经常会在这儿犯错。p->next+指针在完成第一步操作之后，已经不再指向结点 b 了，而是指向结点 x。第 2 行代码相当于将 x 赋值给 x->next，自己指向自己。因此，整个链表也就断成了两半，从结点 b 往后的所有结点都无法访问到了。

# 技巧3：利用哨兵简化实现难度

在结点p后面插入一个新的结点：
```python
new_node.next = p.next
p.next = new_node
```
当要向一个空链表中插入第一个结点：
```python
new_code.next = p
```

删除p的后继结点操作：
```python
p.next = p.next.next
```
删除最后一个结点：
```python
p.next = None
```

**针对链表的插入、删除操作，需要对插入第一个结点和删除最后一个结点的情况进行特殊处理。**

# 技巧4：重点留意边界条件处理

检查链表代码是否正确的边界条件：
- 如果链表为空时，代码是否能正常工作
- 如果链表只包含一个结点时，代码是否能正常工作
- 如果链表只包含两个结点时，代码是否能正常工作
- 代码逻辑在处理头结点和尾结点时候，能否能正常工作

# 技巧5：举例画图，辅助思考

![画图发](https://img2018.cnblogs.com/blog/1256425/201810/1256425-20181005120252681-1705580262.png)

# 技巧6：多写多练，没有捷径

1. 单链表反转
```python
class Nodelist:
    def __init__(self, node):
    self.node = node
    self.next = None
```
```python
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev.next, cur = prev, cur, cur.next
        return prev
```

2. 链表中环的检测
```python
class Nodelist:
    def __init__(self, node):
    self.node = node
    self.next = None
```
```python
class Solution:
    def has_cycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
```

3. 两个有序的链表合并
```python
class Nodelist:
    def __init__(self, node):
    self.node = node
    self.next = None
```
```python
class Solution:
    def merge_two_nodelist(self, head1, head2):
        node = ListNode(None)
        listnode = node
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 != None:
            node.next = l1
        if l2 != None:
            node.next = l2
        return listnode.next
```

4. 删除链表倒数第n个结点
```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = head
        end = head
        for _ in range(n):
            end = end.next
        if end is None:  # 需要删除的节点为第一个节点时，即返回第二个节点为头节点的链表
            return head.next
        while end.next is not None:
            pre = pre.next
            end = end.next
        pre.next = pre.next.next 
        return head
```
第二种方法：
```python
'''可以使用类似求倒数第k的节点的方式，使用等距法'''
        
        if head == None:
            return None
        
        p1 = head
        p2 = head 
        # 使用try结构，表示如果链表长度不够n，就不用删除，直接返回首节点即可
        try:
            for i in range(n):
                p2=p2.next
        except:
            return head
        
        # 如果长度恰好等于n，就返回以第二个节点为首节点的链表
        if p2==None:
            return head.next
        
        # 循环直到p2指向最后一个节点
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        del_node = p1.next
        p1.next = p1.next.next
        del del_node
        return head
```

5. 求链表的中间结点

快慢指针法：当用慢指针 slow 遍历列表时，让另一个指针 fast 的速度是它的两倍。当 fast 到达列表的末尾时，slow 必然位于中间。
```python
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
