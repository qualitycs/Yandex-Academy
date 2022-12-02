n = int(input())
includesCat = False
for i in range(n):
    string = input()
    if 'Кот' in string or 'кот' in string:
        includesCat = True
if includesCat is True:
    print('МЯУ')
else:
    print('НЕТ')
