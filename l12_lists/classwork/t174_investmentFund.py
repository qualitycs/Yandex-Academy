investmentList = []
returnsList = []
n = int(input())
for i in range(n):
    investment = int(input())
    investmentList.append(investment)
    returnsList.append(investment * 3)
print(*investmentList, sep='\n')
print('\n', sep='', end='')
print(*returnsList, sep='\n')
