houseSum = 0
unique = True
allHouses = []
n = int(input())
for i in range(n):
    houses = input().split(' - ')
    allHouses.append(houses)
num = input()
for houses in allHouses:
    for house in houses:
        unique = True
        for k in num:
            if k in house:
                unique = False
        if unique is True:
            houseSum += int(house)
    print(houseSum)
    houseSum = 0
# This task actually activated my autism
