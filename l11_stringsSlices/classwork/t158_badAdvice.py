adviceList = []
for i in range(int(input())):
    advice = input().split()
    if advice[0].lower() == 'не':
        advice = ' '.join(advice[1:])
    else:
        advice = ' '.join(advice)
    adviceList.append(advice)
print(*adviceList, sep='\n')
