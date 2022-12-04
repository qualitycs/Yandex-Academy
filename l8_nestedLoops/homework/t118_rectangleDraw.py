b = int(input())
a = int(input())
symbol = input()
print(symbol * a)
for i in range(b - 2):
    print(symbol, ' ' * (a - 2), symbol, sep='')
print(symbol * a)
