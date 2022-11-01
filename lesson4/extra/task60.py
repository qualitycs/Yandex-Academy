num = int(input())
while num % 10 == 0:
    print(num)
    num = int(input())
while num % 10 != 0:
    try:
        input()
    except EOFError:
        quit()
