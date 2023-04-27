def get_opposite_color(r, g, b):
    return 255 - r, 255 - g, 255 - b


r, g, b = map(int, input().split())
opposite_r, opposite_g, opposite_b = get_opposite_color(r, g, b)
print(opposite_r, opposite_g, opposite_b)
