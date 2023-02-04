pi = 3.14159


def circle_length(radius):
    return 2 * pi * radius


def circle_area(radius):
    return pi * radius * radius


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))
