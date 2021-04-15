"""
CP1404 Practical
State names in a dictionary
Count the occurrences of words in a string
"""
word_to_count = {}
text = input("Text: ")
words = text.split()
print(words)
for word in words:
    number_of_words = word_to_count.get(word,0)
    word_to_count[word] = number_of_words +1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))