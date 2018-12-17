def bigger_price(limit, data):
    sort = sorted(data, key = lambda x: x['price'], reverse = True)
    return sort[:limit]
