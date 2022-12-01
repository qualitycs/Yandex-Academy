import math
pi = math.pi
n = int(input())
inverseSquaresSum = 0
for k in range(1, n + 1):
    inverseSquare = 1 / pow(k, 2)
    inverseSquaresSum += inverseSquare
print(pow(pi, 2) / inverseSquaresSum)
