result = [1, 1, 1]
limit = int(input())
while 1:
    if len(result) >= limit:
        break
    new = sum(result[-3:])
    result.append(new)
if limit == 1:
    print('1')
elif limit == 2:
    print('1 1')
else:
    print(*result)
