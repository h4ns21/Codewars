# First method

def sum_mix(arr):    
    total = 0
    for element in arr:
    # checking whether its a number or not
        if isinstance(element, int) or element.isdigit() or str(element):
        # adding the element to the total
            total += int(element)
    return total

# Second method

def sum_mix(arr):
    return sum(map(int, arr))

# Third method

def sum_mix(arr):
    return sum(int(n) for n in arr)
