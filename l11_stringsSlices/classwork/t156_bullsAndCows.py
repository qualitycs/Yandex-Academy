word1, word2, bulls, cows, counter = input(), input(), 0, 0, 0
for letter in word2:
    if letter in word1 and word1[counter] == letter:
        bulls += 1
    elif letter in word1:
        cows += 1
    counter += 1
print(bulls, cows)
