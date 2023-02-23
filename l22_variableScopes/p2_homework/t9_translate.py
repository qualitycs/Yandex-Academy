translated_text = ""


def translate(text):
    global translated_text
    translated_text = ' '.join(''.join(c for c in text if c not in 'АаЕеЁёИиОоУуЫыЭэЮюЯя.!?,:;-\'"').split())
    return translated_text
