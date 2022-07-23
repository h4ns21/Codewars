# First solution

```python
def maps(a):
    return [i + i for i in a]  # double list using list comprehension
```

# Second solution

```python
def maps(a):
    return map(lambda x:2*x, a)
```
