import unittest
# https://leetcode.com/problems/reverse-linked-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hare = head
        tortoise = head

        while hare and tortoise and hare.next:
            if hare == tortoise:
                return True
            hare = hare.next.next
            tortoise = tortoise.next

        return False
