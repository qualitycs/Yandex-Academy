plaintext = int(input())
digit1 = plaintext // 10 ** 3 % 10
digit2 = plaintext // 10 ** 2 % 10
digit3 = plaintext // 10 ** 1 % 10
digit4 = plaintext // 10 ** 0 % 10
if digit4 > digit3 > digit2 > digit1:
    print(str(digit1) + str(digit2) + str(digit3) + str(digit4))
