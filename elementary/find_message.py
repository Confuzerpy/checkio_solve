import re

def find_message(text):
    return ''.join(re.findall(r'[A-Z]', text))
