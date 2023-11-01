def findFactorialRecursive(number: int):
    if number < 2:
        return 1
    return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number):
    answer = 1
    for i in range(number, 0, -1):
        answer = answer * i
    return answer


print(findFactorialRecursive(5))
print(findFactorialIterative(5))
