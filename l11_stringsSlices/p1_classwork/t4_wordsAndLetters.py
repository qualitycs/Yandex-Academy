yes = True
wordList = []
while True:
    word = input()
    if word == 'стоп':
        break
    wordList.append(word)
shortestWord = sorted(wordList, key=len)[0]
longestWord = sorted(wordList, key=len)[-1]
for letter in shortestWord:
    if letter not in longestWord:
        yes = False
if yes is True:
    print('ДА')
else:
    print('НЕТ')
