num = input()
digits = sorted([int(num[0]), int(num[1]), int(num[2])])
if (digits[0] + digits[2]) / 2 == digits[1]:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
