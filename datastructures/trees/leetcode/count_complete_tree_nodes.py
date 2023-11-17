# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        tree_height = self.get_tree_height(root)
        if tree_height == 0:
            return 1

        upper_count = (2**tree_height)-1
        left_index = 0
        right_index = upper_count
        while left_index < right_index:
            index_to_find = self.find_mid(left_index, right_index)
            if self.node_exists(index_to_find, tree_height, root):
                left_index = index_to_find
            else:
                right_index = index_to_find - 1

        return upper_count + left_index + 1

    def get_tree_height(self, root):
        level_counter = 0

        while root.left:
            level_counter += 1
            root = root.left

        return level_counter

    def node_exists(self, index_to_find, tree_height, node):
        left = 0
        right = (2**tree_height) - 1
        count = 0
        while count < tree_height:
            mid_of_node = self.find_mid(left, right)

            if index_to_find >= mid_of_node:
                node = node.right
                left = mid_of_node
            else:
                node = node.left
                right = mid_of_node - 1
            count += 1
        return not node

    def find_mid(self, a, b):
        return ((a+b)//2) + 1
