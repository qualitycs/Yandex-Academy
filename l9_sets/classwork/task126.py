half = False
half1 = set()
half2 = set()
while half is False:
    houseNum = input()
    if houseNum == '':
        half = True
    else:
        half1.add(houseNum)
while half is True:
    houseNum = input()
    if houseNum == '':
        break
    else:
        half2.add(houseNum)
same = half1.intersection(half2)
if same:
    print(*same, sep='\n')
else:
    print('EMPTY')
