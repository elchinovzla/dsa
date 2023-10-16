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


myBST = MyTree()
myBST.insert(9)
myBST.insert(4)
myBST.insert(6)
myBST.insert(20)
myBST.insert(170)
myBST.insert(15)
myBST.insert(1)
print(myBST.root)
print(myBST.lookup(4))
print(myBST.lookup(20))
print(myBST.lookup(6))
print(myBST.lookup(19))
myBST.remove(9)
print("=================\nafter removing root\n=================\n", myBST.root)
