n = int(input())
q, s, k = 1, 1, 0
while q <= n:
    print(q, end=' ')
    q += 1
    k += 1
    if k == s:
        print()
        s += 1
        k = 0
