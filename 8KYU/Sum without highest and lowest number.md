# First solution

```python
import numpy as np

def sum_array(arr):
    if not arr or len(arr) < 3:  # None or empty
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)  # Sum without highest and lowest number
```

# Second solution

```python
def sum_array(arr):
    if not arr or len(arr) < 3:  # None or empty
        return 0
    return sum(arr) - max(arr) - min(arr)
```
