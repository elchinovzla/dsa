# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root, 0)

    def traverse(self, node, max_depth_nodes):
        if not node:
            return max_depth_nodes
        max_depth_nodes += 1

        return max(self.traverse(node.left, max_depth_nodes),
                   self.traverse(node.right, max_depth_nodes))
