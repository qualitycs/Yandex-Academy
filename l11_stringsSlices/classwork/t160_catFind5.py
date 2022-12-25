n = int(input())
count = 0
g = 0
for i in range(n):
    word = input()
    count += 1
    g = 0
    if 'кот' in word or 'Кот' in word:
        for j in word:
            if j == 'к' and word[g + 1] == 'о':
                print(count, g + 1)
            else:
                g += 1
    else:
        continue
