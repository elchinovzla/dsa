from functools import reduce


def multiply_by_2(item):
    return item * 2


def is_odd(item):
    return item % 2 is not 0


def accumulator(acc, item):
    return acc + item


my_list = [1, 2, 3]
my_list_times_two = list(map(multiply_by_2, my_list))
print(my_list)
print('map - multiply by 2:', my_list_times_two)
print('filter - remove even numbers:', list(filter(is_odd, my_list)))
print('zip:', list(zip(my_list, my_list_times_two)))
print('reduce:', reduce(accumulator, my_list, 0))
