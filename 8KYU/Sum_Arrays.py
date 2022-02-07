# First method

def sum_array(a):
    s = 0
    for i in range(0,len(a)):
        s = s + a[i];
    return s

# Second method

def sum_array(a):
  return sum(a)
