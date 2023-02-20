name = ''


def polite_input(question):
    global name
    if name == '':
        name = input('Как вас зовут?\n')
    polite_question = f'{name}, {question}'
    return input(polite_question + '\n')
