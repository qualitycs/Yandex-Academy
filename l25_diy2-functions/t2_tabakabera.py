def parchment(word, divisor=' '):
    global snuffbox
    snuffbox = tuple(divisor.join(set(item) - set(word)) for item in snuffbox)
