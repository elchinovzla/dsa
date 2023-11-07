# same as arrays
print("PART 1")
basket = [1, 2, 3, 4, 5, 3, 33]
basket.insert(0, 99)
basket.extend([100])
print(basket)
basket.pop()
basket.pop(0)
print(basket)
print(basket.index(3))
print(4 in basket)
print(19 in basket)
print(basket.count(3))
print(sorted(basket))
copy_basket = basket.copy()
basket.clear()
print(basket)
copy_basket.reverse()
print(copy_basket)
print(copy_basket[::-1])
print("************************\n")

print("PART 2")
print(" ".join(["hello", "world!"]))
print("************************\n")

print("PART 3 - unpacking")
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
print("************************\n")

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of {char} is: {i}')

print("PART 4 - Comprehension")
print([char for char in "hello"])
print([num for num in range(0, 5)])
print([num*2 for num in range(0, 5)])
print([num*2 for num in range(0, 5) if num % 2 == 0])
