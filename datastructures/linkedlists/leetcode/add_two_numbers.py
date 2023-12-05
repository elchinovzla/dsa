# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_size = self.get_size(l1)
        l2_size = self.get_size(l2)

        if l1_size > l2_size:
            result = l1
        else:
            result = l2

        res = 0
        head = result

        while result:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + res

            if val > 9:
                res = 1
                result.val = val - 10
            else:
                res = 0
                result.val = val

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if result.next is None and res > 0:
                result.next = ListNode(1)
                result = result.next
            else:
                result = result.next

        return head

    def get_size(self, ll):
        size = 0
        while ll:
            size += 1
            ll = ll.next

        return size
