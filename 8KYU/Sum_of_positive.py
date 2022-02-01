# First method

def positive_sum(arr):
    s = 0
    for x in arr:
        if x > 0:
            s += x
    return s

# Second method

def positive_sum(arr):
    return sum(x for x in arr if x > 0)
