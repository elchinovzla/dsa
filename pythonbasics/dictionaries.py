# same as map

dictionary_1 = {
    'a': 1,
    'b': 2
}

print(dictionary_1['b'])

dictionary_2 = {
    'c': 21,
    '0': 12
}
list = [dictionary_1, dictionary_2]
print(list)
print(list[1]['0'])

dictionary = {
    123: [1, 2, 3],
    'greeting': 'hello',
    'is_magical': True
}
print(dictionary[123])
print(dictionary.get('age', 55))

user = dict(age=23, colour="purple", is_droid=True)
print(user.get('age', 55))
print('age' in user.keys())
print(user.items())
print(user.values())
print(user.keys())
user.update({'ages': 34})
print(user.pop('age'))
print(user)

for key, value in user.items():
    print(key, ": ", value)


print("PART 2 - Comprehension")
simple_dict = {
    'a': 1,
    'b': 2
}
print({key: value*2 for key, value in simple_dict.items() if value % 2 == 0})
print({num: num*2 for num in [1, 2, 3]})
