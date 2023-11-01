def bubbleSort(numbers: [int]):
    collectionLength = len(numbers)
    for i in range(0, collectionLength):
        for j in range(0, collectionLength-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


print(bubbleSort([1, 3, 2, 5, 23, 1, 5, 21, 50, 60,
      0, 12, 435, 123, 12, 12, 34, 23, 12, 7, 5, 7]))
