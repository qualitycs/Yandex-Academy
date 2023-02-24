def matrix(n=-1, m=-1, a=0):
    if m < 0:
        if n < 0:
            n = m = 1
        else:
            m = n
    return [[a for _ in range(m)] for _ in range(n)]
