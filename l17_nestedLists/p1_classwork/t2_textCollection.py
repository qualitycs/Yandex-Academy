selected = list(map(int, input().split()))
words = input().lower().split()
print(' '.join(words[i - 1] for i in selected).capitalize())
