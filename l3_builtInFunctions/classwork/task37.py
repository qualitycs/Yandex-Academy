import numpy

number = float(input())
if -0.000001 < number < 0.000001:
    print(1000000)
else:
    print(numpy.reciprocal(number))
