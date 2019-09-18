# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, low = head, head
        node = head
        pos = 0
        while fast and low and fast.next:
            fast = fast.next.next
            low = low.next
            if fast == low:
                while low != node:
                    node = node.next
                    low = low.next
                return low
        return None