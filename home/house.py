def house(plan):
    plan = plan.split('\n')
    c = []
    count = 0
    plan1 = []
    plan2 = []
    f = 0
    ind2 = 0

    for i in plan:
        if '#' not in i:
            plan1.append(i)
        else:
            for letter in i:
                if letter == '#':
                    ind = i.index(letter)
                    plan1.append(i[ind:])
                    break

    for i in plan1:
        i = i[::-1]
        if '#' not in i:
            plan2.append(i)
        else:
            for letter in i:
                if letter == '#':
                    ind = i.index(letter)
                    plan2.append(i[ind:])
                    break
