def between_markers(text, begin, end):
    if begin in text:
        b_i = text.find(begin) + len(begin)
    else:
        b_i = 0

    if end in text:
        e_i = text.find(end)
    else:
        e_i = len(text)

    return text[b_i:e_i]
