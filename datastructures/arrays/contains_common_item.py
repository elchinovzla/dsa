# Given 2 arrays, create a function that let's a user know (true/false)
# whether these two arrays contain any common items
# For example:
# const array1 = ['a', 'b', 'c', 'x'];
# const array2 = ['z', 'y', 'i'];
# should return false
# ----------------------
# const array1 = ['a', 'b', 'c', 'x'];
# const array2 = ['z', 'y', 'x'];
# should return true

array1 = ['a', 'b', 'c', 'x']
array2_false = ['z', 'y', 'i']
array2_true = ['z', 'y', 'x']


def contains_common_item_brute(arr1, arr2) -> bool:
    """Function checking whether or not the two arrays contain a matching value, 
    using brute force -> O(n*m)"""
    for value1 in arr1:  # O(n)
        for value2 in arr2:  # O(m)
            if value1 == value2:
                return True
    return False


def contains_common_item(arr1, arr2) -> bool:
    """Function checking whether or not the two arrays contain a matching value, 
    without using brute force -> O(n)"""
    arr1_dict = {}

    for value1 in arr1:  # O(n)
        arr1_dict[value1] = True

    for value2 in arr2:  # O(m)
        if value2 in arr1_dict:
            return True
    return False


print("Result with array expecting false using brute:",
      contains_common_item_brute(array1, array2_false))
print("Result with array expecting true using brute:",
      contains_common_item_brute(array1, array2_true))

print("Result with array expecting false:",
      contains_common_item(array1, array2_false))
print("Result with array expecting true:",
      contains_common_item(array1, array2_true))
