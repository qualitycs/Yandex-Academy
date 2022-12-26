interestingCreatures = []
a = int(input())
n = int(input())
for i in range(n):
    creature = int(input())
    if creature % a > 0 and creature not in interestingCreatures:
        interestingCreatures.append(creature)
print('Интересненько! ', end='')
print(*interestingCreatures, sep=' - ')
