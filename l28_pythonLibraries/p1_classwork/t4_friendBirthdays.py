import datetime


def find_birthday(days_left):
    current_date = datetime.date.today()
    birthday_date = current_date + datetime.timedelta(days=days_left)
    return birthday_date.day, birthday_date.month


print(*find_birthday(int(input())))
