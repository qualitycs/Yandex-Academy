heights = []
try:
    while True:
        height = int(input())
        heights.append(height)
except EOFError:
    pass

if heights:
    average_height = sum(heights) / len(heights)
    print(average_height)
else:
    print(-1)
