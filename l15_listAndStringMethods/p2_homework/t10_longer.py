a = input().lower()
print(max(a.count(char) for char in set(a)))
