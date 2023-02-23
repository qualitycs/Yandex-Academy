phrases = []


def parrot(phrase):
    if phrase in phrases:
        print(phrase)
    phrases.append(phrase)
