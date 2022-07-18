# First solution

```python
def get_sum(a,b):
     return sum(range(b, a+1)) if a > b else sum(range(a, b+1)) if b > a else a  # if - elif - else
```

# Second solution

```python
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
```
