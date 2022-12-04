a = "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
b = '1234567890@#–—$_&-+()/*":;!?,.~`|•√π÷×¶∆£¢€¥^°={}\%©®™✓[]<> '
number = int(input())
cipher = str(input())
total = 0
for i in range(len(cipher)):
    for j in range(len(a)):
        if cipher[i] == a[j]:
            j += number + number
            if j > 64:
                j = j - 64
                print(a[j], end="")
            else:
                print(a[j], end="")
    else:
        if cipher[i] in b:
            print(cipher[i], end="")
