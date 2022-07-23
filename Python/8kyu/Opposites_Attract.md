# First method

```python
def lovefunc(f1, f2):
    if (f1 % 2 == 0) and (f2 % 2 != 0) or (f1 % 2 != 0) and (f2 % 2 == 0):
        return True
    else:
        return False
```

# Second method

```python
def lovefunc(f1, f2):
    return (f1+f2)%2
```
