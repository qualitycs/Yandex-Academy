num = int(input())
count = 0
remainder = 0
while num >= 2:
    remainder = num % 2
    num = num / 2
    count += 1
if remainder != 0:
    print('НЕТ')
else:
    print(count)
