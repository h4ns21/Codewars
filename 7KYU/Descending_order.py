def descending_order(n):
    return int(''.join(map(str, sorted([i for i in str(n)], reverse=True))))
