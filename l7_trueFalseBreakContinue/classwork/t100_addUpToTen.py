nSum = 0
count = 0
while True:
    n = int(input())
    nSum += n
    count += 1
    if nSum == 10:
        print(count)
        break
