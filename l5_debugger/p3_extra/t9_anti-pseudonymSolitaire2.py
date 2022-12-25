stones = int(input())
while stones > 0:
    taken = stones % 4
    if taken == 0:
        taken = 2
    stones -= taken
    print(taken, stones)
    if stones == 0:
        print('Вы выиграли!')
    else:
        taken = int(input())
        if 1 <= taken <= 3 and taken <= stones:
            continue
        else:
            while not (1 <= taken <= 3 and taken <= stones):
                print('Некорректный ход:', taken)
                taken = int(input())
        stones -= taken
        print(taken, stones)
        if stones == 0:
            print('ИИ выиграл!')
# Вы выиграли!
# ИИ выиграл!
