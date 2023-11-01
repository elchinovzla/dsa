def selectionSort(numbers):
    collectionLength = len(numbers)

    for i in range(0, collectionLength):
        smallestIndex = i
        temp = numbers[i]
        for j in range(i+1, collectionLength):
            if (numbers[j] < numbers[smallestIndex]):
                smallestIndex = j
        numbers[i] = numbers[smallestIndex]
        numbers[smallestIndex] = temp
    return numbers


print(selectionSort([1, 3, 2, 5, 23, 1, 5, 21, 50, 60,
      0, 12, 435, 123, 12, 12, 34, 23, 12, 7, 5, 7]))
