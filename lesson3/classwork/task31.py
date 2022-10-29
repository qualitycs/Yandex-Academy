city1 = input()
city2 = input()
if (city1 == city2) or (city1 == 'Пенза' and city2 == 'Тула') or (city2 == 'Пенза' and city1 == 'Тула'):
    print('НЕТ')
elif city1 == 'Тула' or city2 == 'Пенза':
    print('ДА')
else:
    print('НЕТ')
# Jenny is the antichrist and I hate her
