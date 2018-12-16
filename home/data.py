def checkio(data):
    list = []

    for i in data:
        if data.count(i) >= 2:
            list.append(i)

    return list
