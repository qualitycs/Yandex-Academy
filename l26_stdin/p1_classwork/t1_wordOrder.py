input_string = input()
words = input_string.split()
sorted_words = sorted(words, key=lambda word: word.lower())
print(" ".join(sorted_words))
