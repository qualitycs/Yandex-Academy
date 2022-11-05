num = int(input())
n1 = 0
n2 = 1
while num >= n1 + n2:
    n1 = n1 + n2
    print(n1)
    n2 = n1 + n2
    print(n2)
