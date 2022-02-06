# First method

def past(h, m, s):
    a = 3600000*h
    b = 60000*m
    c = 1000*s
    return a+b+c
  
# Second method

def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
