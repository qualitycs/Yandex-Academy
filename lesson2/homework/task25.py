print('You are in a room with 3 doorways in it')
print('Input 1 in order to enter the red doorway or input 2 in order to enter the green doorway or input 3 in order to'
      'to enter the blue doorway.')
door = input('What is your choice? ')
if door == '1':
    print('You have entered a small room filled with snakes!')
    print('Input 1 in order to try and kill the snakes, input 2 in order to speak with the snakes.')
    snakeChoice = input('What is your choice? ')
    if snakeChoice == '1':
        print('You failed to kill the snakes and died.')
    elif snakeChoice == '2':
        print('You befriended the snakes and became the snake king. Congratulations, you have scaly friends!')
    else:
        print('error')
elif door == '2':
    print('You enter a dark cave with a fork in it.')
    print('Input 1 in order to enter the path on the left or input 2 in order to enter the path on the right.')
    forkChoice = input('What is your choice? ')
    if forkChoice == '1':
        print('Congratulations, you escaped the labyrinth!')
    elif forkChoice == '2':
        print('You fell into a deep pit and died.')
elif door == '3':
    print('You have entered a room full of gold. Congratulations, you are rich!')
else:
    print('error')
