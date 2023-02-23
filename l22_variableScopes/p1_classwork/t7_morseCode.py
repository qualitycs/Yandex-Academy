MorseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
             'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def encode_to_morse(text):
    result = ''
    for letter in text.upper():
        if letter in MorseCode:
            result += MorseCode[letter] + ' '
    return result


def decode_from_morse(code):
    result = ''
    for sequence in code.split():
        for letter, morse in MorseCode.items():
            if morse == sequence:
                result += letter
                break
    return result


def main():
    choice = input('Do you want to encode or decode the morse code? Write 1 to encode, write 2 to decode:')
    text = input('Input the text you want to decode/encode:')
    if choice == '1':
        print(encode_to_morse(text))
    if choice == '2':
        print(decode_from_morse(text))
