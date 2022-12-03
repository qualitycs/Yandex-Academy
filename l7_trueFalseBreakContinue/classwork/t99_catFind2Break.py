catFound = False
phrase = input()
count = 1
number = 0
while phrase != 'СТОП':
    if 'Кот' in phrase or 'кот' in phrase:
        catFound = True
        number = count
        break
    else:
        catFound = False
    count = count + 1
    phrase = input()
if catFound:
    print(number)
else:
    print(-1)
