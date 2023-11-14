# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        parent_next_node = list()
        current_node = head
        while current_node:
            if current_node.child:
                if current_node.next:
                    parent_next_node.append(current_node.next)
                child_node = current_node.child
                current_node.next = child_node
                current_node.child = None
                child_node.prev = current_node
                current_node = child_node
            else:
                if current_node.next is None:
                    previous_parent_next_node = parent_next_node.pop() if parent_next_node else None
                    if previous_parent_next_node:
                        current_node.next = previous_parent_next_node
                        previous_parent_next_node.prev = current_node
                        current_node = previous_parent_next_node
                    else:
                        current_node = None
                else:
                    current_node = current_node.next
        return head


### Udemy solution###
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        current_node = head
        while current_node:
            if current_node.child:
                tail = current_node.child
                while tail.next:
                    tail = tail.next
                tail.next = current_node.next
                if tail.next:
                    tail.next.prev = tail
                current_node.next = current_node.child
                current_node.next.prev = current_node
                current_node.child = None

            current_node = current_node.next
        return head
