def insertionSort(numbers):
    for i in range(1, len(numbers)):
        valueToInsert = numbers[i]
        j = i - 1
        while j >= 0 and valueToInsert < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = valueToInsert
    return numbers


print(insertionSort([1, 3, 2, 5, 23, 1, 5, 21, 50, 60,
      0, 12, 435, 123, 12, 12, 34, 23, 12, 7, 5, 7]))
