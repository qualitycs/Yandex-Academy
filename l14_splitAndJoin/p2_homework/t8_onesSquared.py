n = int(input())
print(*([R * R for i in range(1, 1000) if (R := int('1' * i)) < n]), sep=', ')
