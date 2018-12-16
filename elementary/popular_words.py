def popular_words(text, words):
    t_low = text.lower()
    spl = t_low.split()
    dct = {}
    for word in words:
        if words.count(word) > 0:
            dct[word] = spl.count(word)
        else:
            dct[word] = 0

    return dct
