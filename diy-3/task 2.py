import datetime

date_str = input().strip()
weeks = int(input().strip())
no_delivery_days = list(map(int, input().strip().split()))
date = datetime.datetime.strptime(date_str, '%m-%d-%Y')

delta = datetime.timedelta(weeks=weeks)
date += delta

while date.weekday() in no_delivery_days:
    date += datetime.timedelta(days=1)
print(date.year, date.strftime('%d %B'))

second_date = date + datetime.timedelta(days=1)
while second_date.weekday() in no_delivery_days:
    second_date += datetime.timedelta(days=1)
print(second_date.year, second_date.strftime('%d %B'))
