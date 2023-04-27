import random
import string


def generate_password(m):
    allowed_chars = string.ascii_letters + string.digits
    forbidden_chars = "lI1oO0"
    allowed_chars = ''.join(c for c in allowed_chars if c not in forbidden_chars)
    return ''.join(random.choice(allowed_chars) for _ in range(m))


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        password = generate_password(m)
        passwords.add(password)
    return list(passwords)
