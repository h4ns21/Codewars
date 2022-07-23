# First solution

```python
def find_short(s):
    l = min(s.split(), key=len)
    return len(l) # l: shortest word length
```

# Second solution

```python
def find_short(s):
    return min(len(x) for x in s.split())
```
