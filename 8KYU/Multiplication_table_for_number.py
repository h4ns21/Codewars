# First method
def multi_table(n):
    out = ""
    for i in range(1,11):
        out += (str(i) + ' * ' + str(n) + ' = ' + str(n*c) + "\n")
    return out.strip()

# Second method
def multi_table(n):
    return '\n'.join(f'{i} * {n} = {i * n}' for i in range(1, 11))
