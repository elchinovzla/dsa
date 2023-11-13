import unittest
# https://leetcode.com/problems/reverse-linked-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False


class Solution(object):
    def reverseList(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current_node = head
        while current_node:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next

        return prev


class Tests(unittest.TestCase):
    def test_reverseList_example1(self):
        solution = Solution()
        node_5 = ListNode(5)
        node_4 = ListNode(4, node_5)
        node_3 = ListNode(3, node_4)
        node_2 = ListNode(2, node_3)
        node_1 = ListNode(1, node_2)

        expected_node_5 = ListNode(1)
        expected_node_4 = ListNode(2, expected_node_5)
        expected_node_3 = ListNode(3, expected_node_4)
        expected_node_2 = ListNode(4, expected_node_3)
        expected_node_1 = ListNode(5, expected_node_2)
        self.assertEqual(solution.reverseList(node_1), expected_node_1)

    def test_reverseList_example2(self):
        solution = Solution()
        node = ListNode(4)
        expected_node = ListNode(4)
        self.assertEquals(solution.reverseList(node), expected_node)

    def test_reverseList_example3(self):
        solution = Solution()
        self.assertEqual(solution.reverseList(None), None)


if __name__ == '__main__':
    unittest.main()
