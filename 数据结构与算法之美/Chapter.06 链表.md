
**链表，通过“指针”将一组零散的内存串联到一起使用**，其中，内存块称为链表的**节点**，记录下一个节点的指针叫做**后继指针next**
![链表和数组的内存分布](https://static001.geekbang.org/resource/image/d5/cd/d5d5bee4be28326ba3c28373808a62cd.jpg)
链表分为：**单链表、双向链表和循环链表**

链表中插入或删除数据的时间复杂度是O(1)。因为链表中的数据是非连续存储的，所以无法像数组那样，根据首地址和下标，拖过寻址公式就能直接计算出对应的内存地址，而是需要根据指针一个节点一个结点依次遍历，知道找到相应的节点，需要**O(n)的时间复杂度**。
![插入和删除节点](https://static001.geekbang.org/resource/image/45/17/452e943788bdeea462d364389bd08a17.jpg)
![单链表](https://static001.geekbang.org/resource/image/b9/eb/b93e7ade9bb927baad1348d9a806ddeb.jpg)
**循环链表是一种特殊的单链表**。它跟单链表唯一的区别就在尾结点，循环指针的尾结点指针指向链表的头结点。
![循环链表](https://static001.geekbang.org/resource/image/86/55/86cb7dc331ea958b0a108b911f38d155.jpg)
双向链表，它支持两个方向，每个结点不止有一个后继指针next指向后面的结点，还有一个前驱指针prev指向前面的结点。
![双向链表](https://static001.geekbang.org/resource/image/cb/0b/cbc8ab20276e2f9312030c313a9ef70b.jpg)
数组的缺点是大小固定，已经声明就要占用整块连续的内存空间。如果声明的数组过大，系统可能没有足够的连续内存给它，导致“内存不足”。如果声明的数组过小，则可能出现不够用的情况，只能再申请一个更大的内存空间，非常费时。而链表没有大小限制，天然地支持动态扩容
![数组vs链表](https://static001.geekbang.org/resource/image/4f/68/4f63e92598ec2551069a0eef69db7168.jpg)

如何实现LRU缓存淘汰算法？(leetcode 147)

维护一个有序单链表，越靠近链表尾部的结点是越早之前访问的。当有一个新的数据被访问时，就从链表头开始顺序遍历链表。
1. 如果此数据之前已经被缓存在链表中了，则遍历链表找到相应的结点，将其从原位置删除后重新插入到链表中
2. 如果此数据没有缓存在链表中
    1. 如果此时缓存未满，则将此节点直接插入到链表的头部
    2. 如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部。

1. 理解指针或引用的含义

不管是指针还是引用，实际上，他们都是一样的，都是存储所指对象的内存地址。**将某个变量赋值给指针，实际上就是将这个变量的地址赋值给指针。或者反过来说，指针中存储的这个变量的内存地址，指向了这个变量，通过指针就能找到这个变量**

2. 警惕指针丢失和内存泄漏

**在插入结点时，一定要注意操作的顺序**，要先将结点x的指针指向结点b，再把结点a的指针指向结点x
![插入结点](https://static001.geekbang.org/resource/image/05/6e/05a4a3b57502968930d517c934347c6e.jpg)
删除链表结点时，一定要记得手动释放内存空间

3. 利用哨兵结点简化实现难度

**针对链表的插入、删除操作，需要对插入第一个结点和删除最后一个结点的情况进行特殊处理**

如果引入哨兵结点，再任何时候，不管链表是不是空，head指针都会一直指向这个哨兵结点。这种有哨兵结点的链表叫做**带头链表**。
![哨兵结点](https://static001.geekbang.org/resource/image/7d/c7/7d22d9428bdbba96bfe388fe1e3368c7.jpg)
4. 重点留意边界条件处理

经常用来检查链表代码是否正确的边界条件
- 如果链表为空
- 如果链表只包含一个结点
- 如果链表只包含两个结点
- 代码逻辑再处理头结点和尾节点的时候

5. 举例画画
![链表操作](https://static001.geekbang.org/resource/image/4a/f8/4a701dd79b59427be654261805b349f8.jpg)

6. 练习
    1. 单链表反转
    2. 链表中环的检测
    3. 两个有序链表合并
    4. 删除链表倒数第n个结点
    5. 求链表的中间结点


```python
# 单链表反转
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        result = None
        while head:
            nextone = head.next
            head.next = result
            result = head
            head = nextone
        return result
```


```python
# 反转链表2
class Solution:
    def reverseBetween(self, head, m: int, n: int):
        result = ListNode(-1)
        result.next = head
        res = result
        for _ in range(m-1):
            res = res.next
        node = None
        cur = res.next
        for _ in range(n-m+1):
            third = cur.next
            cur.next = node
            node = cur
            cur = third
        res.next.next = cur
        res.next = node
        return res
```


```python
# 链表中环的检测:快慢指针
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, low = head, head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
            if low == fast:
                return True
        return False
```


```python
# 两个有序链表合并
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(None)
        result = head
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        if l1 is None:
            head.next = l2
        if l2 is None:
            head.next = l1
        return result.next
```


```python
# 删除链表倒数第n个结点 1
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(None)
        result.next = head
        res = result
        m = 0
        while head:
            m += 1
            head = head.next
        for _ in range(m-n):
            result = result.next
        result.next = result.next.next
        return res.next
```


```python
# 删除链表倒数第n个结点 :快慢指针
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:return 
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        while n:
            fast = fast.next
            n -= 1
        slow = dummy
        while  fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
```


```python
# 求链表的中间结点
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


```python

```
