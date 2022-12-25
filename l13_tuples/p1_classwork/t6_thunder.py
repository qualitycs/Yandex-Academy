n = int(input())
h = [0] * n
p = [0.0] * n
for i in range(n):
    h[i] = int(input())
    p[i] = float(input())
for i in range(n - 1):
    for j in range(i + 1, n):
        if h[j] > h[i] or (h[j] == h[i] and p[j] > p[i]):
            h[i], h[j] = h[j], h[i]
            p[i], p[j] = p[j], p[i]
for i in range(n):
    print((h[i], p[i]))
