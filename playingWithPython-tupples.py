# tupples are immutable
myTupple = ("apple", "banana", "cherry", "banana", "last one")
# myTupple[0] = "sonny" errors out
print(myTupple)

myList = list(myTupple)
myList[0] = "sonny"
myTupple = tuple(myList)
print(myTupple)

(cool, *other, last_one) = myTupple
print(cool)
print(other)
print(last_one)
print(myTupple.count("banana"))
