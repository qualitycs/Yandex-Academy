a = int(input())
b = int(input())
table = []
buffer = []
for i in range(a):
    buffer.clear()
    table.append(list(buffer))
    for j in range(b):
        table[i].append(input())

for i in range(len(table)):
    print("\t".join(table[i]))
