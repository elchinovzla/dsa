def merge_sorted_arrays(array1, array2):
    result = []
    if len(array1) == 0 or len(array2) == 0:
        return array1 + array2

    array1_index = 0
    array2_index = 0

    while (array1_index < len(array1) and array2_index < len(array2)):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    return result + array1[array1_index:] + array2[array2_index:]


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
print(merge_sorted_arrays([], [4, 6, 30]))
print(merge_sorted_arrays([0, 3, 4, 31], []))
print(merge_sorted_arrays([0, 3, 4, 29, 30, 30, 31,
      100], [-1, 0, 1, 2, 3, 4, 6, 30, 99, 101]))
