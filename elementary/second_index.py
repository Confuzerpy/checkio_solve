def second_index(text, ind):
    try:
        a = text.index(ind)
        b = text.index(ind, a+1)
        return b
    except:
        return None
