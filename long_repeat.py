def long_repeat(line):
    line = line.lower()
    max_sub_str = 0
    try:
        a = line[0]
        for i in range(len(line)):
            if line[i] == line[i+1]:
                a += line[i+1]
                max_sub_str = len(a)
            else:
                if len(a) > max_sub_str:
                    max_sub_str = len(a)
                a = line[i+1]

    except IndexError:
        pass

    return max_sub_str
