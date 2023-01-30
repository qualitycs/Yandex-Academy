def golden_ratio(i):
    painlist = []
    a, b = 1, 1
    for j in range(i + 1):
        painlist.append(a)
        a, b = b, a + b
    print(painlist[-1] / painlist[-2])
