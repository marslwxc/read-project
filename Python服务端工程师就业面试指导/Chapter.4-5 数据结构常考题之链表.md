
链表
- 链表涉及到指针操作较为复杂，容易出错，经常用作考题
- 熟悉链表定义和常见操作
- 常考题：删除一个链表节点
- 常考题：合并两个有序链表


```python
# 删除链表中的节点
"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

示例 1:
输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明:
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
"""
class Solution:
    def deleteNode(self, node):
        next_node = node.next
        after_next_node = node.next.next
        node.val = next_node.val
        node.next = after_next_node
```


```python
# 21. 合并两个有序链表
"""
将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
class Solution:
    def mergeTwoLists(self, l1, l2):
        root = ListNode(None)
        cur = root
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            cur.next = node
            cur = node
        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1
        return root.next
```
