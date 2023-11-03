class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        msg = ""
        msg += "node: " + (str(self.value) if self.value else "None") + "\n"
        msg += "left node: " + (str(self.left.value)
                                if self.left else "None") + "\n"
        msg += "right node: " + (str(self.right.value)
                                 if self.right else "None") + "\n"
        return msg


class MyTree:
    def __init__(self) -> None:
        self.root = None

    def findParentNode(self, value):
        currentNode = self.root
        parentNode = None
        while currentNode is not None:
            if value == currentNode.value:
                currentNode = None
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                parentNode = currentNode
                currentNode = currentNode.left

        return parentNode

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            parentNode = self.findParentNode(value)
            if value > parentNode.value:
                parentNode.right = newNode
            else:
                parentNode.left = newNode

    def getCurrentNode(self, value, parentNode):
        if parentNode is None:
            return self.root
        elif value > parentNode.value:
            return parentNode.right
        elif value < parentNode.value:
            return parentNode.left

    def lookup(self, value):
        parentNode = self.findParentNode(value)
        return self.getCurrentNode(value, parentNode)

    def removeNodeWithoutRightNode(self, node, parentNode):
        if parentNode is None:
            self.root = node.left
        elif node.value < parentNode.value:
            parentNode.left = node.left
        elif node.value > parentNode.value:
            parentNode.right = node.left

    def removeNodeWithRightNodeWithNoLeftNode(self, node, parentNode):
        if parentNode is None:
            self.root = node.left
        else:
            node.right.left = node.left
            if node.value < parentNode.value:
                parentNode.left = node.right

    def removeNodeWithRightNodeWithLeftNode(self, node, parentNode):
        leftMostParent = self.getLeftMostParentNode(node)
        leftMost = leftMostParent.left
        leftMostParent.left = leftMost.right
        leftMost.left = node.left
        leftMost.right = node.right

        if parentNode is None:
            self.root = leftMost
        elif node.value < parentNode.value:
            parentNode.left = leftMost
        elif node.value > parentNode.value:
            parentNode.right = leftMost

    def getLeftMostParentNode(self, node):
        leftMost = node.right.left
        leftMostParent = node.right
        while leftMost.left is not None:
            leftMostParent = leftMost
            leftMost = leftMost.left

        return leftMostParent

    def remove(self, value):
        if self.root is None:
            return None

        parentNode = self.findParentNode(value)
        currentNode = self.getCurrentNode(value, parentNode)
        if currentNode.right is None:
            self.removeNodeWithoutRightNode(currentNode, parentNode)
        elif currentNode.right.left is None:
            self.removeNodeWithRightNodeWithNoLeftNode(currentNode, parentNode)
        else:
            self.removeNodeWithRightNodeWithLeftNode(currentNode, parentNode)

    def bfs(self):
        currentNode = self.root
        answer = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            answer.append(currentNode.value)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
        return answer

    def bfsRecursive(self, queue, answer):
        if len(queue) == 0:
            return answer

        currentNode = queue.pop(0)
        answer.append(currentNode.value)
        if currentNode.left is not None:
            queue.append(currentNode.left)
        if currentNode.right is not None:
            queue.append(currentNode.right)

        return self.bfsRecursive(queue, answer)

    def traverseInOrder(self, node, answer):
        if node.left:
            self.traverseInOrder(node.left, answer)
        answer.append(node.value)
        if node.right:
            self.traverseInOrder(node.right, answer)
        return answer

    def dfsInOrder(self):
        return self.traverseInOrder(self.root, [])

    def traversePreOrder(self, node, answer):
        answer.append(node.value)
        if node.left:
            self.traversePreOrder(node.left, answer)
        if node.right:
            self.traversePreOrder(node.right, answer)
        return answer

    def dfsPreOrder(self):
        return self.traversePreOrder(self.root, [])

    def traversePostOrder(self, node, answer):
        if node.left:
            self.traversePostOrder(node.left, answer)
        if node.right:
            self.traversePostOrder(node.right, answer)
        answer.append(node.value)
        return answer

    def dfsPostOrder(self):
        return self.traversePostOrder(self.root, [])


myBST = MyTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(20)
myBST.insert(170)
myBST.insert(15)
myBST.insert(1)
#       9
#   4       20
# 1   6  15    170

# bfs is good for shortest path
print("breadth first search:", myBST.bfs())
print("breadth first search using recursion:",
      myBST.bfsRecursive([myBST.root], []))
# for depth first search, the sorting can be done as: in order, pre order, and post order
# dfs is good to check if it exists
print("depth first search in order:", myBST.dfsInOrder())
print("depth first search pre order:", myBST.dfsPreOrder())
print("depth first search post order:", myBST.dfsPostOrder())
