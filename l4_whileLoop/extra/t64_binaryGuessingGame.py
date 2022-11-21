low = 1
high = 1000
while True:
    guess = int((low + high) / 2)
    print(guess)
    a = input()
    if a == '=':
        quit()
    elif a == '<':
        high = guess - 1
    elif a == '>':
        low = guess + 1
