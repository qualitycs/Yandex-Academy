def find_mountain(heightsMap):
    row = -1
    maxvalue = 0
    for i in heightsMap:
        if max(i) > maxvalue:
            maxvalue = max(i)
    for i in heightsMap:
        row += 1
        column = -1
        for j in i:
            column += 1
            if j == maxvalue:
                return row, column
