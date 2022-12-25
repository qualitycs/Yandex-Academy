stringList = []
searchList = []
stringCount = int(input())
for i in range(stringCount):
    string = input()
    stringList.append(string)
searchCount = int(input())
for j in range(searchCount):
    search = input()
    searchList.append(search)
for string in stringList:
    if all(search in string for search in searchList):
        print(string)
