string = input()
n = int(input())
if n < 1 or n > len(string):
    print('ОШИБКА')
else:
    print(string[n - 1])
