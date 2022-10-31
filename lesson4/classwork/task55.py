count = 0
height = input()
heightList = []
while height != '!':
    if 190 >= int(height) >= 150:
        heightList.append(height)
        count += 1
    height = input()
print(count)
print(sorted(heightList)[0], sorted(heightList)[-1])
