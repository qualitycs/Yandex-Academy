daily_food = [0, 150, 150]


def count_food(days: list):
    return sum([daily_food[i - 1] for i in days])
