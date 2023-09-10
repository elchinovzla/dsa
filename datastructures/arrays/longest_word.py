# https://coderbyte.com/editor/Longest%20Word:Python3
def LongestWord(sen):
    words = sen.split(" ")
    clean_words(words)
    return get_longest_word(words)


def clean_words(words):
    for index, word in enumerate(words):
        words[index] = "".join(filter(str.isalnum, word))


def get_longest_word(clean_words):
    longest_word = ""
    for word in clean_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(LongestWord("fun&!! time"))
