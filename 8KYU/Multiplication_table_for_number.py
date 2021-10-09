def multi_table(n):
    out = ""
    for c in range(1,11):
        out += (str(c) + ' * ' + str(n) + ' = ' + str(n*c) + "\n")
    return out.strip()
