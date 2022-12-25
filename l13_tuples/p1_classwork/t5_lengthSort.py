strings = []
n = int(input())
for i in range(n):
    string = input()
    strings.append(string)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(strings[j]) > len(strings[j + 1]):
            strings[j], strings[j + 1] = strings[j + 1], strings[j]
        elif len(strings[j]) == len(strings[j + 1]):
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
print(*strings, sep='\n')
