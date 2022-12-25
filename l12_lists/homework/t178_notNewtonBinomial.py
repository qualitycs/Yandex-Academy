nums = []
n = int(input())
for i in range(n):
    number = int(input())
    nums.append(number)
for j in range(n):
    if j + 2 > n:
        break
    print(nums[j] + nums[j + 1])
