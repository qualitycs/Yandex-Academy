from random import randint
stones = int(input())

while stones > 0:
    ai_subtract = randint(1, 3)
    if stones < 7:
        ai_subtract = randint(2, 3)
    if stones < 4:
        ai_subtract = stones
        print(stones, 0)
        print('ИИ выиграл!')
        quit()
    stones = stones - ai_subtract
    print(ai_subtract, stones)
    player_subtract = int(input())
    while player_subtract > 3 or player_subtract < 1 or player_subtract > stones:
        print('Некорректный ход:', player_subtract)
        player_subtract = int(input())
    stones = stones - player_subtract
    print(player_subtract, stones)
print('Вы выиграли!')
