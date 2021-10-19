# First method
def get_count(sentence):
    count = 0
    vowels = set('AaEeIiOoUu')
    for c in sentence:
        if c in vowels:
            count += 1
    return count

# Second method
def getCount(s):
    return sum(c in 'aeiouAEIOU' for c in s)
