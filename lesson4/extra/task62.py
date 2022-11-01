doorFailed = True
snakeFailed = True
forkFailed = True

print('You are in a room with 3 doorways in it')
print('Input 1 in order to enter the red doorway or input 2 in order to enter the green doorway or input 3 in order to'
      ' enter the blue doorway.')
while doorFailed is True:
    door = input('What is your choice? ')
    if door == '1':
        doorFailed = False
        print('You have entered a small room filled with snakes!')
        print('Input 1 in order to try and kill the snakes, input 2 in order to speak with the snakes.')
        while snakeFailed is True:
            snakeChoice = input('What is your choice? ')
            if snakeChoice == '1':
                snakeFailed = False
                print('You failed to kill the snakes and died.')
            elif snakeChoice == '2':
                snakeFailed = False
                print('You befriended the snakes and became the snake king. Congratulations, you have scaly friends!')
            else:
                snakeFailed = True
    elif door == '2':
        doorFailed = False
        print('You enter a dark cave with a fork in it.')
        print('Input 1 in order to enter the path on the left or input 2 in order to enter the path on the right.')
        while forkFailed is True:
            forkChoice = input('What is your choice? ')
            if forkChoice == '1':
                forkFailed = False
                print('Congratulations, you escaped the labyrinth!')
            elif forkChoice == '2':
                forkFailed = False
                print('You fell into a deep pit and died.')
            else:
                forkFailed = True
    elif door == '3':
        doorFailed = False
        print('You have entered a room full of gold. Congratulations, you are rich!')
    else:
        doorFailed = True
