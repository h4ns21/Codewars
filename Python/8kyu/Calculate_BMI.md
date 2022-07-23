# First method

```python
def bmi(weight, height):
    x = weight/(height*height)
    if x <= 18.5:
        return "Underweight"
    elif x <= 25.0:
        return "Normal"
    elif x <= 30.0:
        return "Overweight"
    elif x > 30:
        return "Obese"
```

 # Second method

```python
 def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
```
