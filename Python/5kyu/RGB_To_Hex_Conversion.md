# First solution

```python
def rgb(r, g, b):
    def help(t):  # function to help us to round to the nearest valid number
        if t < 0: return 0
        if t > 255: return 255
        return t
    
    r = help(r)
    g = help(g)
    b = help(b)
    
    return '%02X%02X%02X' % (r, g, b)
```

# Second solution

```python
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
```
