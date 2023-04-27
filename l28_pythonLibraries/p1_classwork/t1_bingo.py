import random


def make_bingo():
    numbers = list(range(1, 76))
    random.shuffle(numbers)
    card = [[0] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if row == 2 and col == 2:
                card[row][col] = 0
            else:
                card[row][col] = numbers.pop()

    return tuple(tuple(row) for row in card)
