# First method
def simple_multiplication(number):
    if number % 2 == 0:
        return number*8
    else:
        return number*9

# Second method
def simple_multiplication(number):
    return number * (8 if number % 2 == 0 else 9)
