number = int(input())
while number != 0:
    print(number)
    number = int(input())
while number == 0:
    try:
        input()
    except EOFError:
        quit()
