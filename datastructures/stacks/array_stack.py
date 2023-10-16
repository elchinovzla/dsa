class ArrayStack:
    def __init__(self) -> None:
        self.list = []
        self.top_index = -1

    def push(self, value):
        self.list.append(value)
        self.top_index += 1

    def peek(self):
        return None if not self.list else self.list[self.top_index]

    def pop(self):
        if not self.list:
            return None
        self.top_index -= 1
        return self.list.pop()


test = ArrayStack()
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
