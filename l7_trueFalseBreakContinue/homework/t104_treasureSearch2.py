x1, y1, x, y, count = 0, 0, int(input()), int(input()), 0
while not (x1 == x and y1 == y):
    world_side, n = input(), int(input())
    count += 1
    if world_side == 'север':
        y1 += n
    elif world_side == 'юг':
        y1 -= n
    elif world_side == 'запад':
        x1 -= n
    elif world_side == 'восток':
        x1 += n
print(count)
