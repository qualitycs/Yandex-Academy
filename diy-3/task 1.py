import random


names = input().split()
n = int(input())
w_min, w_max = map(int, input().split())

selected_names = random.sample(names, n)

for name in selected_names:
    weight = random.randint(w_min, w_max)
    area = round(random.uniform(0.1, 12.5), 1)
    resistance = round(weight * 10 / area)

    print(f"{name.capitalize()} with weight {weight} kg, area {area} cm2, resistance {resistance}.")
