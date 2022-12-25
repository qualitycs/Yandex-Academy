stringList = []
letterList = []
n = int(input())
for i in range(n):
    string = input()
    stringList.append(string)
position = int(input())
for string in stringList:
    if len(string) < position:
        letterList.append('')
    else:
        letterList.append(string[position - 1])
print(*letterList, sep='')
