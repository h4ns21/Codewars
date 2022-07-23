# First solution

```python
def disemvowel(string_):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return ''.join([i for i in string_ if i not in vowels])
```

# Second solution

```python
def disemvowel(string):
    return ''.join(c for c in string if c.lower() not in "aeiou")
```
