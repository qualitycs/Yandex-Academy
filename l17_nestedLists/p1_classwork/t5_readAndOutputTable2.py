table = []
rows, columns = int(input()), int(input())
for i in range(rows):
    b = []
    for j in range(columns):
        b.append(input())
    table.append(b)
for i in table:
    for j in range(columns - 1):
        print(i[j], end='\t')
    print(i[-1])
print()
for i in range(columns):
    for j in range(rows - 1):
        print(table[j][i], end='\t')
    print(table[-1][i])
