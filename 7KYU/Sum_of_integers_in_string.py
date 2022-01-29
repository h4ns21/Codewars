# First method

def sum_of_integers_in_string(n):
    t = "0"
    sum = 0
    for ch in n:
        if ch.isdigit():
            t += ch
        else:
            sum += int(t)
            t = "0"
    return sum + int(t)

# Second method

import re

def sum_of_integers_in_string(s):
    return sum(int(x) for x in re.findall(r"(\d+)", s))
