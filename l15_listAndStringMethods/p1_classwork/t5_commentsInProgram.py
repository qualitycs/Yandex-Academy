formattedLines = []
n = int(input()[1:])
for i in range(n):
    line = input()
    if '#' in line:
        a = line.find('#')
        line = line[0:a]
    line = line.rstrip()
    formattedLines.append(line)
print(*formattedLines, sep='\n')
