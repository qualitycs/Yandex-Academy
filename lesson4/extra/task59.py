password = input()
check = input()
if len(password) < 8:
    print('Короткий!')
elif '123' in password:
    print('Простой!')
elif password != check:
    print('Различаются.')
else:
    print('OK')
