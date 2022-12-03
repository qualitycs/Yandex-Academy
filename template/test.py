k = int(input())
for j in range(1, 10):
    if j == k:
        continue
    for i in range(1, 10):
        print(i, '*', j, '=', j * i, sep='', end='\t')
    print()
