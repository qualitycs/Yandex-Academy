def transpose(matrix):
    temp = [list(row) for row in zip(*matrix)]
    while matrix:
        matrix.pop(-1)
    matrix.extend(temp)
