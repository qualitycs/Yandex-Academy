milkQuantityList = []
n = int(input())
for i in range(n):
    milkQuantity = int(input())
    milkQuantityList.append(milkQuantity)
minimum = int(input())
maximum = int(input())
for j in milkQuantityList:
    if minimum <= j <= maximum:
        print(j)
