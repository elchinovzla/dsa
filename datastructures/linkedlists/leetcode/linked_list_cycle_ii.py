# https://leetcode.com/problems/linked-list-cycle-ii/description/

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
        tortoise = head
        hare = head
        while tortoise and hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                tortoise = head
                while tortoise != hare:
                    tortoise = tortoise.next
                    hare = hare.next
                return tortoise
        return None
