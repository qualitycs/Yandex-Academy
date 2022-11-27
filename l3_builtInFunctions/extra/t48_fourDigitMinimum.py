num = int(input())
b = num // 1000
c = num % 1000
d = c // 100
e = c % 100
f = e // 10
g = e % 10
if b > d:
    b, d = d, b
if d > f:
    d, f = f, d
if f > g:
    f, g = g, f
if b > d:
    b, d = d, b
if d > f:
    d, f = f, d
if b > d:
    b, d = d, b
if b == 0 and d:
    b, d = d, b
elif b == 0 and f:
    b, f = f, b
elif b == 0 and g:
    b, g = g, b
print(b, d, f, g, sep='')
