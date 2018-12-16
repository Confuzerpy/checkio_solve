import re

def first_word(text):
    if text[0] == ' ':
        text = text.lstrip()
        text = re.match(r'([A-Za-z]+)', text)
        return text.group(0)
    elif text[0] == '.':
        text = text.lstrip('.')
        text = text.lstrip()
        text = re.match(r'([A-Za-z]+)', text)
        return text.group(0)
    else:
        if "'" in text:
            text = text.split()
            text = text[0]
            return str(text)
        else:
            text = re.match(r'([A-Za-z]+)',text)

            return text.group(0)
