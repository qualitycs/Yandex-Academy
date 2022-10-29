name = input('Назовите себя, пожалуйста! \n')
entry = input('Введите текст. \n')
repetition = input('Повторите текст. \n')
if entry == repetition:
    print(name + ', введено верно!')
else:
    print(name + ', пока не получилось, попробуйте снова!')
