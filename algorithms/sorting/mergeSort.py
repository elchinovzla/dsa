def mergeSort(numbers):
    if len(numbers) == 1:
        return numbers

    half = len(numbers)//2
    left = numbers[: half]
    right = numbers[half:]

    return merge(
        mergeSort(left),
        mergeSort(right)
    )


def merge(left, right):
    mergedCollection = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            mergedCollection.append(left[leftIndex])
            leftIndex += 1
        else:
            mergedCollection.append(right[rightIndex])
            rightIndex += 1

    mergedCollection += left[leftIndex:]
    mergedCollection += right[rightIndex:]
    return mergedCollection


print(mergeSort([1, 3, 2, 5, 23, 1, 5, 21, 50, 60, 0,
      12, 435, 123, 12, 12, 34, 23, 12, 7, 5, 7, 19]))
