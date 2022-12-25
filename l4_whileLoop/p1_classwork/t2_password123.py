password1 = input()
password2 = input()
if len(password1) < 8:
    print('Короткий!')
    quit()
elif password1 != password2:
    print('Различаются.')
else:
    print('OK')
