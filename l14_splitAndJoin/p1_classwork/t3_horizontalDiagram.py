string = input()
lengths = ['*' * int(n) for n in string.split()]
print(*lengths, sep='\n')
