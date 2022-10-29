plaintext = int(input())
digit1 = plaintext // 10 ** 2 % 10
digit2 = plaintext // 10 ** 1 % 10
digit3 = plaintext // 10 ** 0 % 10
part1 = digit1 + digit2
part2 = digit2 + digit3
if part2 > part1:
    print(str(part2) + str(part1))
elif part1 > part2:
    print(str(part1) + str(part2))
