```python
def find(n):
    return sum(i for i in range(n+1) if not i % 3 or not i % 5)
```
