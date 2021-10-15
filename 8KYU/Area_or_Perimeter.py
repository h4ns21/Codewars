# First method
def area_or_perimeter(l , w):
    area = l*l
    perimeter = 2*(l+w)
    if l == w:
        return area
    else:
        return perimeter

# Second method
def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2
