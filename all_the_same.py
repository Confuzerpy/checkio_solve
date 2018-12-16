from typing import List, Any

def all_the_same(lst):
    if len(lst) < 1:
        return True
    elif len(lst) == lst.count(lst[0]):
        return True
    else:
        return False
