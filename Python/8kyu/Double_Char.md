# First method

```python
def double_char(s):
    outs = ''
    for i in s:
        outs = outs + i + i
    return outs
```

# Second method

```python
def double_char(s):
    return ''.join([c+c for c in s])  # (c*2 for c in s)
```
