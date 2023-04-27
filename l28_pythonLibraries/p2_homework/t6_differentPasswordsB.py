import string
import random


def generate_password(m):
    safe_chars = string.ascii_lowercase.replace('l', '').replace('o', '') + string.ascii_uppercase.replace('I',
                                                                                                           '').replace(
        'O', '') + string.digits.replace('1', '').replace('0', '')

    while True:
        password = ''.join(random.choices(safe_chars, k=m))
        if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(
                char.isdigit() for char in password):
            return password


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(m)
        passwords.add(password)
    return list(passwords)
