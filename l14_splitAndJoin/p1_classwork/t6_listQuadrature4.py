print(*([int(i) ** 2 for i in input().split() if int(i) ** 2 % 10 != 9 and int(i) % 2 > 0]))
