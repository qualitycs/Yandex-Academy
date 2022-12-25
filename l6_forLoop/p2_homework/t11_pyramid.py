width = 1
height = int(input())
for i in range(0, height):
    print(int((1 + 2 * (height - 1) - width) / 2) * ' ' + '*' * width)
    width += 2
