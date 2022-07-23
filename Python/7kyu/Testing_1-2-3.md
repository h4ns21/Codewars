# First solution

```python
def number(lines):
    return [] if not lines else [f'{i+1}: {v}' for i, v in enumerate(lines)]
```
# Second solution

```python
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
```
