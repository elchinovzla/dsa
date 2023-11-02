def quickSort(numbers):
    return sort(numbers, 0, len(numbers)-1)


def sort(numbers, low, high):
    if (low < high):
        partitionIndex = partition(numbers, low, high)
        sort(numbers, low, partitionIndex - 1)
        sort(numbers, partitionIndex+1, high)


def partition(numbers, low, high):
    pivot = numbers[high]
    i = low - 1
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1


data = [1, 3, 2, 5, 23, 1, 5, 21, 50, 60, 0,
        12, 435, 123, 12, 12, 34, 23, 12, 7, 5, 7, 19]
quickSort(data)
print(data)
