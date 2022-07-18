# First option

```python
def reverse_seq(n):
    mine = list(range(1, n+1))
    return mine[::-1]
```

# Second option

```python
def reverse_seq(n):
    return range(n, 0, -1)
```
