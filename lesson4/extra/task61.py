Failed = True
while Failed is True:
    password = input()
    check = input()
    if len(password) < 8:
        Failed = True
        print('Короткий!')
    elif '123' in password:
        Failed = True
        print('Простой!')
    elif password != check:
        Failed = True
        print('Различаются.')
    else:
        Failed = False
print('OK')
