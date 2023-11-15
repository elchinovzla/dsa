# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue(object):

    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)
        return None

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        elif self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        elif self.stack_out:
            temp = self.stack_out.pop()
            self.stack_out.append(temp)
            return temp
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            temp = self.stack_out.pop()
            self.stack_out.append(temp)
            return temp

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
