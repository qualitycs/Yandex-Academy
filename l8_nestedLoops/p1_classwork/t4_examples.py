a, b, c = int(input()), int(input()), int(input())
for i in range(a, b + 1, c):
    for j in range(a, b + 1, c):
        print(f'{i} + {j} = {i + j}', end='')
        if j != b + c:
            print('\t', end='')
    if i != b + c:
        print('\n', end='')
