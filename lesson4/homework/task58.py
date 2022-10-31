num = int(input())
count = 0
while num >= 2:
    num = num / 2
    if num % 2 > 0:
        count = 'НЕТ'
    count += 1
print(count)
