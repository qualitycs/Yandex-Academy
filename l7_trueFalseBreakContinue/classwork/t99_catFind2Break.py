count = 0
finalCount = 0
locked = False
while True:
    string = input()
    if string == 'СТОП':
        break
    if 'Кот' in string or 'кот' in string:
        count += 1
        break
if count > 0:
    print(count)
else:
    print('-1')
