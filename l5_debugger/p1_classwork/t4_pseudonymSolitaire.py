num = int(input())
while num > 0:
    subtract = int(input())
    if subtract > 3 or subtract < 1 or subtract > num:
        subtract = 0
    num = num - subtract
    print(num)
