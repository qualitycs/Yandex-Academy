string = input()
length = len(string)
print(string)
for i in range(length // 2 + 1):
    string = string[1:length - 1]
    length = len(string)
    print(string)
