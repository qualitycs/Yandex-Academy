half1 = set()
half2 = set()
stop = False

houseNum = input()
while houseNum != '':
    houseNum = input()
    half1.add(houseNum)
stop = True
houseNum = input()
while stop is True and houseNum != '':
    houseNum = input()
    half2.add(houseNum)

same = half1.intersection(half2)
if same:
    print(*same, sep='\n')
else:
    print('EMPTY')
