import unittest
# https://leetcode.com/problems/reverse-linked-list-ii/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head is None:
            return None

        node_counter = 1
        current_node = head
        prev_node = head

        while node_counter < left and current_node:
            prev_node = current_node
            current_node = current_node.next
            node_counter += 1

        reverted_nodes = None
        reverted_nodes_tail = current_node

        while node_counter >= left and node_counter <= right and current_node:
            next = current_node.next
            current_node.next = reverted_nodes
            reverted_nodes = current_node

            current_node = next
            node_counter += 1

        prev_node.next = reverted_nodes
        reverted_nodes_tail.next = current_node

        return head if left > 1 else reverted_nodes


class Tests(unittest.TestCase):
    def test_reverseBetween_example1(self):
        solution = Solution()
        node_5 = ListNode(5)
        node_4 = ListNode(4, node_5)
        node_3 = ListNode(3, node_4)
        node_2 = ListNode(2, node_3)
        node_1 = ListNode(1, node_2)

        expected_node_5 = ListNode(5)
        expected_node_4 = ListNode(2, expected_node_5)
        expected_node_3 = ListNode(3, expected_node_4)
        expected_node_2 = ListNode(4, expected_node_3)
        expected_node_1 = ListNode(1, expected_node_2)
        self.assertEqual(solution.reverseBetween(
            node_1, 2, 4), expected_node_1)

    def test_reverseBetween_example2(self):
        solution = Solution()
        node = ListNode(5)
        expected_node = ListNode(5)
        self.assertEquals(solution.reverseBetween(node, 1, 1), expected_node)

    def test_reverseBetween_example3(self):
        solution = Solution()
        self.assertEqual(solution.reverseBetween(None, 1, 1), None)


if __name__ == '__main__':
    unittest.main()
