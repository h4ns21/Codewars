# First method
def find_multiples(integer, limit):
    res = [i for i in range(integer, limit+1, integer)] 
    return res

# Second method
def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
