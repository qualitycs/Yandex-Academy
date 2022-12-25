s = 'a'
waves_before_higher = []
for i in range(int(input())):
    temp = input()
    if s[-1] < temp[-1]:
        waves_before_higher.append((i, s[:-2]))
    s = temp
print(*waves_before_higher, sep='\n')
