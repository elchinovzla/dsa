# order collection of unique objects
my_set = {1, 2, 3, 5, 6, 4, 6, 6}
print(my_set)
my_set.add(100)
print(my_set)
print(len(my_set))

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8, 9, 10}
print("difference:", set_1.difference(set_2))
set_1.discard(3)
print("discard:", set_1)
# set_1.difference_update(set_2)
# print("difference upodate", set_1)
print("intersection:", set_1.intersection(set_2))
print("is disjoint:", set_1.isdisjoint(set_2))
print("union:", set_1.union(set_2))
print("union using or:", set_1 | set_2)  # same as union
print("is subset:", set_1.issubset(set_2))
print("is super set:", set_1.issuperset(set_2))


print("PART 2 - Comprehension")
print(set(char for char in "hello"))
print(set(num for num in range(0, 5)))
print(set(num*2 for num in range(0, 5)))
print(set(num*2 for num in range(0, 5) if num % 2 == 0))
