def checkio(words):
    count = 0
    if len(words) == 2 or len(words) == 3:
        return False
    else:
        for i in words.split():
            if i.isalpha():
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False
