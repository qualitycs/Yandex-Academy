sources = []
sounds = []
n = int(input())
for i in range(n):
    sound = input().lower()
    sounds.append(sound)
source = 'empty'
while source != '':
    source = input().upper()
    sources.append(source)
print('{')
for sound in sounds:
    similarity = 0
    applicableSources = []
    for source in sources:
        if similarity >= 3 and len(source) <= len(sound):
            applicableSources.append(source)
        for letter in sources:
            if letter.upper() in sound:
                similarity += 1
    if len(applicableSources) == 0:
        print('  ""' + sound + '"":', '"source"', end='')
    print('""' + sound + '"":', '"' + source + '"', end='')
    if sounds.index(sound) == len(sounds):
        break
    else:
        print(',', end='')
    print('\n', end='')
print('}')
