num = int(input())
count = 0
grocery_list = []
while count != num:
    grocery_list.append(input())
    count += 1
[print(i) for i in grocery_list]
