numbers = []
goodSum = 0
goodsSums = []
goodNum = True
n = int(input())
for i in range(n):
    nums = input().split(' - ')
    numbers.append(nums)
num = input()
for nums in numbers:
    for k in nums:
        if goodNum is True:
            goodSum += int(k)
        for j in nums:
            if j in num:
                goodNum = False
        goodNum = True
    goodsSums.append(goodSum)
print(goodsSums)
