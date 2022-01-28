import math
def am_i_wilson(n):
    return n > 1 and bool(n == 2 or (n % 2 and (math.factorial(n - 1) + 1) % n == 0))
