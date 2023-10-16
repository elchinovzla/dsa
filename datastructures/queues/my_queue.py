class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next_val = None

    def __str__(self) -> str:
        return "None" if self.value is None else str(self.value)


class LinkedListQueue:
    # FIFO
    def __init__(self) -> None:
        self.top = None
        self.tail = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.tail = newNode
            self.length += 1
        elif self.length > 0:
            self.tail.next_val = newNode
            self.tail = newNode
            self.length += 1

    def peek(self):
        return None if self.top is None else self.top.value

    def pop(self):
        node = self.top
        if self.length > 1:
            second_node = node.next_val
            self.top = second_node
            self.length -= 1
        else:
            self.tail = None
            self.top = None
            self.length = 0

        return node


test = LinkedListQueue()
test.push(5)
test.push(13)
test.push(7)
print(test.peek())
print(test.pop())
test.peek()
print(test.pop())
test.peek()
print(test.pop())
print(test.peek())
