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
