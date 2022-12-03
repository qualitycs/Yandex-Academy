goodCount, badCount = 0, 0
lastGood, lastBad = False, False
string = 'cock'
while string != '':
    string = input()
    if string == 'добрый':
        goodCount += 1
        lastGood = True
        lastBad = False
    if string == 'злой':
        badCount += 1
        lastBad = True
        lastGood = False
    if string == 'Какой подарок?':
        if goodCount > badCount and lastGood is True:
            print('серебряный шиллинг')
        elif badCount > goodCount and lastBad is True:
            print('золотой')
        else:
            print('Ах, не знаю!')
            break
        goodCount, badCount = 0, 0
        lastGood, lastBad = False, False
