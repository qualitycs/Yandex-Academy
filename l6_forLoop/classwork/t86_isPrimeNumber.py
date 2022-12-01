primeCount = 0
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        if n == i:
            print(i)
        else:
            print(i, end=' ')
        if i != n and i != 1:
            primeCount += 1
        else:
            continue
if primeCount != 0 or n == 1:
    print('НЕТ')
else:
    print('ПРОСТОЕ')
