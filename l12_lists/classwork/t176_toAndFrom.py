addendList = []
n = int(input())
for i in range(n):
    addend = int(input())
    addendList.append(addend)
total = 0
for num in addendList[int(input()) - 1: int(input())]:
    total += num
print(total)
