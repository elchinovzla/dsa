def fibonacciArray(index):
    arr = [0, 1]
    for i in range(2, index+1):
        arr.append(arr[i-1] + arr[i-2])

    return arr[index]


def fibonacciIterative(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    indexMinus1 = 1
    indexMinus2 = 0
    i = 2
    while i <= index:
        answer = indexMinus1 + indexMinus2
        indexMinus2 = indexMinus1
        indexMinus1 = answer
        i += 1
    return answer


def fibonacciRecursive(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    return fibonacciRecursive(index - 1) + fibonacciRecursive(index - 2)


print(fibonacciArray(40))
print(fibonacciIterative(40))
print(fibonacciRecursive(40))
