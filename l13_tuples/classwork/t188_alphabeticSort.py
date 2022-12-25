strings = []
n = int(input())
for i in range(n):
    string = input()
    strings.append(string)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if (strings[j]) > strings[j + 1]:
            strings[j], strings[j + 1] = strings[j + 1], strings[j]
print(*strings, sep='\n')
