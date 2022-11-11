n = 1
k = int(input())
for j in range(n, k + 1):
    n += 1
    for i in range(1, n):
        print(i, sep=' ', end='')
    print()
