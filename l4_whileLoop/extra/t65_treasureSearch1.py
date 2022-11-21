# восток = east = (x +=)
# запад = west = (x -=)
# север = north = (y +=)
# юг = south = (y -=)
destination_x = input()
destination_y = input()
directions = ['y+=', 'x-=', 'y-=', 'x+=']
x, y = 0, 0
while destination_y != y and destination_x != x:
    command = input()
    while command != 'вперёд':
        if command == 'налево':
            directions.append(directions.pop(0))
        if command == 'направо':
            directions.insert(0, directions.pop)
        if command == 'разворот':
            directions.insert(1, directions.pop)
    steps = input()
    direction = directions[0]
    exec(direction + steps)
    # I'm pretty sure that using exec is completely unsafe and probably slow, but the code looks nicer this way lmao
    print(x, y)
