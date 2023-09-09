# Create a function that reverses a string:
# 'Hi, my name is Sonny' should be:
# '!ynnoS si eman ,iH'

def reverse_string(string_to_reverse: str):
    reversed_str = ""
    if string_to_reverse is None:
        return

    for char in string_to_reverse:
        reversed_str = char + reversed_str
    print(reversed_str)


def reverse_string_with_slice(string_to_reverse: str):
    if string_to_reverse is None:
        return
    print(string_to_reverse[::-1])


reverse_string("'Hi, my name is Sonny!")
reverse_string("")
reverse_string(None)
reverse_string_with_slice("'Hi, my name is Sonny!")
reverse_string_with_slice("")
reverse_string_with_slice(None)
