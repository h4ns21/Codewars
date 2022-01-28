# FIrst method

def shortcut(s):
    for i in "aeiou":
        s = s.replace(i,"")
    return s
 
# Second method

def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')
 
# Third method

def shortcut(s):
    return s.translate(None, 'aeiou')
