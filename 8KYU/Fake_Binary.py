# First method

def fake_bin(x):
    return ''.join('0' if int(a) < 5 else '1' for a in x)
  
# Second method

import string
def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))
