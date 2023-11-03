class Fibonacci:
    def __init__(self) -> None:
        self.memo = {}
        self.counter = 0

    def fibonacci(self, index):
        if index in self.memo:
            return self.memo[index]

        self.counter += 1
        if index < 2:
            return index
        self.memo[index] = self.fibonacci(
            index - 1) + self.fibonacci(index - 2)
        return self.memo[index]


fib = Fibonacci()
print(fib.fibonacci(40))
print("counter:", fib.counter)
print(fib.fibonacci(4))
print("counter:", fib.counter)
print(fib.fibonacci(34))
print("counter:", fib.counter)
print(fib.fibonacci(4))
print("counter:", fib.counter)
print(fib.fibonacci(50))
print("counter:", fib.counter)
print(fib.fibonacci(80))
print("counter:", fib.counter)
print(fib.fibonacci(100))
print("counter:", fib.counter)
