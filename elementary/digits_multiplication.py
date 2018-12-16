def checkio(num):
    num1 = 1
    for i in str(num):
        if i == '0':
            pass
        else:
            num1 *= int(i)
    return num1
