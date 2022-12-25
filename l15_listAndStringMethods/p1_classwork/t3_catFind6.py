s = [input() for i in range(int(input()))]
for i in range(len(s)):
    if "кот" in s[i]:
        print(i + 1, s[i].find("кот") + 1)
