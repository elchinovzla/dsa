# sets are unchangeable, but you can remove and add items - do not allow duplicates - they are unordered
mySet = {"apple", "banana", "cherry"}
mySet.add("orange")
print(mySet)

mySet.remove("orange")
print(mySet)

# no error if no found, remove does throw error if no found
mySet.discard("sonny")
print(mySet)

setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}
setA.intersection_update(setB)
print(setA)

setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple", "cherry"}
print(setA.intersection(setB))
