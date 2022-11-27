x = int(input())
y = int(input())
xy_map = [x, y]
t = 0
p = ['север', 'запад', 'юг', 'восток']
xy = [0, 0]
command = ''
a = 0
while xy != xy_map:
    command = input()
    a += 1
    if t == 4:
        t = 0
    if t == -1:
        t = 3
    if command == "вперёд":
        xyt = int(input())
        if t == 0:
            xy[1] += xyt
        if t == 1:
            xy[0] -= xyt
        if t == 2:
            xy[1] -= xyt
        if t == 3:
            xy[0] += xyt
    if command == "налево":
        t += 1
    if command == "направо":
        t -= 1
    if command == "разворот":
        t += 2
print(a)
print(p[t])
