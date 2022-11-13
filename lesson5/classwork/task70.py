from random import *
stones = int(input())
while stones > 0:
    ai_subtract = randint(1, 3)
    stones = stones - ai_subtract
    print(ai_subtract, stones)
    player_subtract = int(input())

