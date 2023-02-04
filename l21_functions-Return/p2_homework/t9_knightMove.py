def possible_turns(cell):
    ltn = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    def celltotuple(cell):
        return ltn[cell[0]], int(cell[1])

    def tupletocell(tup):
        return str(get_key(ltn, tup[0])) + str(tup[1])

    def check_tuple(tup):
        return 0 < tup[0] < 9 and 0 < tup[1] < 9

    def moves(tup):
        mvs = []
        a, b = tup
        mvs.append((a + 1, b + 2))
        mvs.append((a - 1, b + 2))
        mvs.append((a + 1, b - 2))
        mvs.append((a - 1, b - 2))
        mvs.append((a + 2, b + 1))
        mvs.append((a + 2, b - 1))
        mvs.append((a - 2, b + 1))
        mvs.append((a - 2, b - 1))
        return mvs

    turns = []
    t = celltotuple(cell)
    lst = moves(t)
    for x in lst:
        if check_tuple(x):
            turns.append(tupletocell(x))
    return sorted(turns)
