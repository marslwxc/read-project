# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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