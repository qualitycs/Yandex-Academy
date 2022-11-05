# восток = east = (x +=)
# запад = west = (x -=)
# север = north = (y +=)
# юг = south = (y -=)
destination_x = input()
destination_y = input()
directions = ['y +=', 'x -=', 'y -=', 'x +=']
x, y = 0, 0
while destination_y != y and destination_x != x:
    command = input()
    if command != 'вперёд':
        if command == 'налево':
            directions.append(directions.pop(0))
        if command == 'направо':
            directions.insert(0, directions.pop)
        if command == 'разворот':
            directions.insert(1, directions.pop)

