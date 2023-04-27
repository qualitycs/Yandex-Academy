import random
import string


def generate_password(m):
    safe_characters = string.ascii_letters.replace("l", "").replace("I", "").replace("o", "").replace("O", "")\
                      + string.digits.replace("1", "").replace("0", "")
    password = ''.join(random.sample(safe_characters, m))
    return password


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(m)
        passwords.add(password)
    return list(passwords)
