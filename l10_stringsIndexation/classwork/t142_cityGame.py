sameLetter = True
city1 = input()
while sameLetter is True:
    city2 = input()
    if city1[-1] != city2[0]:
        print(city2)
        sameLetter = False
    city1 = city2
