def best_stock(data):
    n = list(data.keys())
    p = list(data.values())
    return n[p.index(max(p))]
