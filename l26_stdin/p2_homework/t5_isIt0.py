import sys

print(any(0 in map(int, line.split()) for line in sys.stdin))
