s = [int(input()) for i in range(int(input()))]
for i in range(len(s) - 1):
    for x in range(len(s) - i):
        j = x + i
        if s[j] > s[i]:
            s[i], s[j] = s[j], s[i]
print(*[i for i in s], sep='\n')
