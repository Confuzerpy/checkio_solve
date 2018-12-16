def correct_sentence(text):
    text1 = text[1:]
    text = text[0].upper()
    text = text+text1
    if text[-1] == '.':
        return text
    else:
        return text + '.'
