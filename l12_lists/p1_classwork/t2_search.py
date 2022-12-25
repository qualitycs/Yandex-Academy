stringList = []
n = int(input())
for i in range(n):
    string = input()
    stringList.append(string)
search = input()
for string in stringList:
    if search in string:
        print(string)
