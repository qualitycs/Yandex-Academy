def who_are_you_and_hello():
    while True:
        name = input()
        try:
            if name[0].isupper() is True and name[:0].islower() is True and name.isalpha() is True:
                print('Привет, ', name, '!', sep='')
                break
        except EOFError as name:
            print('', end='')
