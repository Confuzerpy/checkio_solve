def checkio(array):
    if len(array) == 0:
        return 0
    else:
        array1 = array[-1]
        srez = array[::2]
        res = sum(srez) * array1

        return res
