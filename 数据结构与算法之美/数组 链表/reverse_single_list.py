"""
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        while cur != None:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        return prev

"""
def reverseList(self, head):
    cur, prev = head, None
    while cur != None:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
"""