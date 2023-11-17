# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.bfs(root)

    def bfs(self, root):
        if not root:
            return []

        queue = [root]
        result = []
        while queue:
            level_nodes = []
            level_nodes_len = len(queue)
            for _ in range(level_nodes_len):
                current_node = queue.pop(0)
                level_nodes.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(level_nodes.pop())

        return result

    def dfs(self, root):
        if not root:
            return []

        return self.traverse(root, [], 0)

    def traverse(self, node, answer, level):
        if node:
            level += 1
        if level > len(answer):
            answer.append(node.val)
        if node.right:
            self.traverse(node.right, answer, level)
        if node.left:
            self.traverse(node.left, answer, level)

        return answer
