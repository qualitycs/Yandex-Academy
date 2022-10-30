num = input()

nzeros = num.count('0')
num = ''.join(sorted(num.replace('0', '')))
print(num[0] + ('0' * nzeros) + num[1:])
