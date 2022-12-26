def build_pyramid(cube):
    """Построение пирамиды
    максимальной высоты из
    элементов массива cubes,
    элементы берутся только
    справа или слева."""
    tower = [max(cube)]
    n = len(cube)
    for j in range(n):
        left_elem = cube[0]
        right_elem = cube[-1]
        if left_elem > right_elem:
            greed_choice = left_elem
            cube.pop(0)
        else:
            greed_choice = right_elem
            cube.pop()
        if greed_choice > tower[-1]:
            return None
        else:
            tower.append(greed_choice)
    return tower[1:]


t = int(input())
for i in range(t):
    cubes = [int(x) for x in input().split()]
    pyramid = build_pyramid(cubes)
    if pyramid is None:
        print("НЕТ")
    else:
        print(*pyramid)
