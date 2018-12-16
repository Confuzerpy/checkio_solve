def index_power(array, n):
    count = 0
    if n == 0:
        return 1
    elif n >= len(array):
        return -1
    elif array[0] == 0:
        array.remove(0)
        count += array[n] ** n
        return count
    else:
        count += array[n] ** n
        return count
