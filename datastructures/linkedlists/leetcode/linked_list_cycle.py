import unittest
# https://leetcode.com/problems/linked-list-cycle/description/


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
        hare = head
        tortoise = head

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                return True

        return False
