catFound = False
count = 0
phrase = ''
while phrase != 'СТОП':
    phrase = input()
    count += 1
    if not catFound:
        if 'Кот' in phrase or 'кот' in phrase:
            catFound = True
            number = count
if catFound:
    print(number)
else:
    print(-1)
