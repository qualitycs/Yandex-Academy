count = 0
finalCount = 0
locked = False
while True:
    string = input()
    count += 1
    if string == 'СТОП':
        break
    if 'Кот' in string or 'кот' in string:
        if locked is False:
            finalCount = count
            locked = True
if count > 0:
    print(count)
else:
    print('-1')
