n = int(input())
m = int(input())
for i in range(n, 32, m):
    print(n, end=' ')
    n += m
