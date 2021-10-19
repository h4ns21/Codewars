def get_count(sentence):
    count = 0
    vowels = set('AaEeIiOoUu')
    for c in sentence:
        if c in vowels:
            count += 1
    return count
