num = int(input())
count = 0
cities = set()
while num != count:
    cities.add(input())
    count += 1
city = input()
if city in cities:
    print('TRY ANOTHER')
else:
    print('OK')
