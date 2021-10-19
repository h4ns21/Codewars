# First method
def update_light(current):
    return 'yellow' if current == 'green' else 'green' if current == 'red' else 'red'

#Second method
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]
