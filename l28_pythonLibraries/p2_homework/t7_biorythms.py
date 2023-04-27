import datetime
import math


def calculate_biorhythms(birth_date, target_date):
    periods = [23, 28, 33]
    delta = target_date - birth_date
    days_passed = delta.days

    biorhythms = []

    for period in periods:
        value = math.sin(2 * math.pi * days_passed / period) * 100
        biorhythms.append(round(value, 2))

    return biorhythms


birth_date_input = input().strip()
target_date_input = input().strip()
birth_date = datetime.datetime.strptime(birth_date_input, "%d.%m.%Y")
target_date = datetime.datetime.strptime(target_date_input, "%d.%m.%Y")

biorhythms = calculate_biorhythms(birth_date, target_date)

for value in biorhythms:
    print(value)
