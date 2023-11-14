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
        seen_nodes = set()
        current_node = head
        while current_node:
            if current_node in seen_nodes:
                return True
            seen_nodes.add(current_node)
            current_node = current_node.next
        return False
