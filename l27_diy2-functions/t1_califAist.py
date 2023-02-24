import sys
st = []
for line in sys.stdin:
    st.append(line.rstrip('\n'))

print(*max(([x for x in map(int, a.split()) if x % 7 == 0] for a in st), key=len), sep=', ')
