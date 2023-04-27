def ask_password(login, password, success, failure):
    login = login.lower()
    password = password.lower()

    vowels = "aeiouy"
    password_vowels = [char for char in password if char in vowels]
    password_consonants = [char for char in password if char not in vowels]

    login_consonants = [char for char in login if char not in vowels]

    error_vowels = len(password_vowels) != 3
    error_consonants = password_consonants != login_consonants
    error_message = ""

    if error_vowels and error_consonants:
        error_message = "Everything is wrong"
    elif error_vowels:
        error_message = "Wrong number of vowels"
    elif error_consonants:
        error_message = "Wrong consonants"

    if error_message:
        failure(login, error_message)
    else:
        success(login)


def main(login, password):
    def success(login):
        print(f"Привет, {login}!")

    def failure(login, error_message):
        print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку:"
              f" {error_message.upper()}.")

    ask_password(login, password, success, failure)
