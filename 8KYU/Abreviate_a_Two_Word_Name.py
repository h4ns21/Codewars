def abbrev_name(name):
    names = name.split(' ')
    return '.'.join([f"{n[0]}" for n in names]).upper()
