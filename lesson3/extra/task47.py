num = int(input())
digit1 = num // 10 ** 2 % 10
digit2 = num // 10 ** 1 % 10
digit3 = num // 10 ** 0 % 10
half = (digit1 + digit3) / 2
if half == digit2:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
