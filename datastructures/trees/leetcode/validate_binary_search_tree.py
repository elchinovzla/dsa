# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        return self.traverse(root, None, None, True)

    def traverse(self, node, lt, gt):
        is_current_valid = True
        is_left_valid = True
        is_right_valid = True

        if lt is not None and node.val >= lt:
            is_current_valid = False
        if gt is not None and node.val <= gt:
            is_current_valid = False

        if node.left:
            is_left_valid = self.traverse(node.left, node.val, gt)
        if node.right:
            is_right_valid = self.traverse(node.right, lt, node.val)

        return is_current_valid and is_left_valid and is_right_valid
