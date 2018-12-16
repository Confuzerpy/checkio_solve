import re
def checkio(text):
    text = text.lower()
    text = re.sub(r'[^a-z]','', text)
    my_dict = {}

    for i in text:
        my_dict[i] = text.count(i)

    my_list = sorted(my_dict.items(), key=lambda x: x[1])

    if my_list[-1][1] == my_list[0][1]:
        my_list = sorted(my_dict.items(), key=lambda x: x)
        return my_list[0][0]
    return my_list[-1][0]
