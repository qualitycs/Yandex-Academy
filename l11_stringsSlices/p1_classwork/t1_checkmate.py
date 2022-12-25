n = int(input())
letters = 'ABCDEFGHI'
for i in reversed(range(1, n + 1)):
    for j in range(1, n + 1):
        print(letters[j - 1], i, sep='', end=' ')
    print('\n', end='')
