"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(-1)
        result.next = head
        res = result
        for _ in range(m-1):
            res = res.next
        cur, prev = res.next, None
        for _ in range(n-m+1):
            cur.next, prev, cur = prev, cur, cur.next
        res.next.next = cur
        res.next = prev
        return result.next