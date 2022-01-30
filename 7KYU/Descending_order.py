# First method

def descending_order(n):
    return int(''.join(map(str, sorted([i for i in str(n)], reverse=True))))

# Second method

def Descending_Order(n):
    return int(''.join(sorted(str(n), reverse=True)))
