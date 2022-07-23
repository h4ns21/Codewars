# First method

```python
def grow(arr):
    r = 1
    for x in arr:
        r = r * x 
    return r
```

# Second method

```python
import math as m
def grow(arr):
    return m.prod(arr)
```

# Third method

```python
def grow(arr):
    return eval('*'.join([str(i) for i in arr]))
```
