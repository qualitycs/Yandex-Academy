announcementList = []
n = int(input())
announcement = ''
for i in range(n):
    announcement = input()
    announcementList.append(announcement)
quantitySelected = int(input())
selectedList = []
for j in range(quantitySelected):
    selection = int(input())
    selectedList.append(announcementList[selection - 1])
print(*selectedList, sep='\n')
