phrase = ''
n = 0
cat = -1
count = 1
while phrase != 'СТОП':
    phrase = input()
    if 'Кот' in phrase or 'кот' in phrase:
        n += 1
    if ('Кот' in phrase or 'кот' in phrase) and cat == -1:
        cat = count
    count += 1
print(n, cat)
