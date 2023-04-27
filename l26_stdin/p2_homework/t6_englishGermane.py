def gematria(word):
    word = word.upper()
    return sum(ord(c) - ord('A') + 1 for c in word)


words = []

try:
    while True:
        word = input().strip()
        if not word:
            break
        words.append(word)
except EOFError:
    pass

sorted_words = sorted(words, key=lambda x: (gematria(x), x))

for word in sorted_words:
    print(word)
