count = 0
temperature = float(input())
total = 0
while temperature >= -300:
    total = temperature + total
    count += 1
    temperature = float(input())
print(total / count)
