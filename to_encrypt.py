from string import ascii_letters
alfavit = ascii_letters.lower()
alfavit = sorted(list({i for i in ascii_letters.lower()}))

def to_encrypt(text, delta=3):
    text = text.lower()
    shifr = ""
    for letter in text:
        if letter in alfavit:
            ind = alfavit.index(letter)%len(alfavit)
            shifr += alfavit[(ind + delta)%len(alfavit)]
        else:
            shifr += letter

    return shifr
