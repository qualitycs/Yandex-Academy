headlineList = []
maxLength = int(input())
n = int(input())
for i in range(n):
    headline = input()
    if len(headline) > maxLength:
        headline = headline[:maxLength - 3] + '...'
    headlineList.append(headline)
print(*headlineList, sep='\n')
