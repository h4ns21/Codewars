# First method
def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if current_year == year_of_birth:
        return 'You were born this very year!'
    elif current_year == year_of_birth + 1:
        return 'You are ' + str(age) + ' year old.'
    elif current_year > year_of_birth:
        return 'You are ' + str(age) + ' years old.'
    elif current_year + 1 == year_of_birth:
        return 'You will be born in ' + str(abs(age)) + ' year.'
    else: # current_year < year_of_birth:
        return 'You will be born in ' + str(abs(age)) + ' years.'
        
# Second method
def calculate_age(year_of_birth, current_year):
    year = current_year - year_of_birth
    if year > 1: return f'You are {year} years old.'
    if year == 1: return f'You are {year} year old.'
    if year == -1: return f'You will be born in {abs(year)} year.'
    if year < 0: return f'You will be born in {abs(year)} years.'
    else: return 'You were born this very year!'
