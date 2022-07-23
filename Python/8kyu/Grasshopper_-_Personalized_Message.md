# First solution

```python
def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'
```

# Second solution

```python
def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")
```
