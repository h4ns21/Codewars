# First solution

```python
def count(string):
    # using set() + count() to get count of each element in string
    return {} if not string else {i : string.count(i) for i in set(string)}
```

# Second solution

```python
def count(string):
    return {i: string.count(i) for i in string}
```
