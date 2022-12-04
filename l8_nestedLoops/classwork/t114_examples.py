a, b, c = map(int, input().split())
[[print(f'{i} + {j} = {i + j}', end='\t') for j in range(a, b + c, c)] for i in range(a, b + c, c)]
