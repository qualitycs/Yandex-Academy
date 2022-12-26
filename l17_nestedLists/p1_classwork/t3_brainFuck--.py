a = list(input())
b = [0] * 30001
count = len(b) // 2
for i in range(len(a)):
    if a[i] == '+':
        b[count] = (b[count] + 1) % 256
    elif a[i] == '-':
        b[count] = (b[count] - 1) % 256
        if b[count] == -1:
            b[count] = 255
    elif a[i] == '>':
        count += 1
    elif a[i] == '<':
        count -= 1
    else:
        print(b[count])
