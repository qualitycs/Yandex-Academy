def space_game(text):
    spaces = text.count(' ')
    if spaces % 2 != 0:
        print('Вы проиграли')
    else:
        print('Вы выиграли')
