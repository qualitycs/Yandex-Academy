lines = []

try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass

comment_lines = list(filter(lambda line: line.lstrip().startswith('#'), lines))
print(len(comment_lines))
