x, y = 0, 0
destination_x = int(input())
destination_y = int(input())
looking = 1, 0
print(looking)
while destination_x != x and destination_y != y:
    direction1 = input()
    axis = y
    if direction1 == 'вперёд':
        steps = int(input())
        x += steps
    else:
        direction2 = input()
        steps = int(input())
        if direction2 == 'налево':
            print()
