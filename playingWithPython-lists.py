array = ['a', 'b', 'c', 'x']
array[1:3] = ["Sonny", "Leo"]
# in js is similar to splice array.splice(2, 0, "Ana"),
# in js another option for the head is to use unshift array.unshift("Ana")
array.insert(2, "Ana")
array.append("y")
array.extend(["z", "za"])
print(array)

copyArrayWithRemove = list(array)
copyArrayWithRemove.remove("z")
copyArrayWithRemove.pop(2)
copyArrayWithRemove.pop()
print(copyArrayWithRemove)

for x in array:
    print(x)

for index, x in enumerate(copyArrayWithRemove):
    print(index, x)

WHILE_INDEX = 0
while WHILE_INDEX < len(array):
    print(WHILE_INDEX, array[WHILE_INDEX])
    WHILE_INDEX += 1

array.sort()
print(array)

array.sort(reverse=True)
print(array)
print(array.count("sonny"))
