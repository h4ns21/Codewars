def sum_mix(list):    
    total = 0
    for element in list:
    # checking whether its a number or not
        if isinstance(element, int) or element.isdigit():
        # adding the element to the total
            total += int(element)
    return total
