lineList = []
s = ''
trollSum = 0
humanSum = 0
while s != "That's all":
    s = input()
    if 'troll' in s or 'Troll' in s:
        trollSum += len(s)
    elif s != "That's all":
        humanSum += len(s)
print(trollSum, humanSum)
