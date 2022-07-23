# First solution

```python
def wave(p):
    if not p:
        return []
    else:
        new = []
        for i, v in enumerate(p):
            if v == " ":
                continue
            else:
                new.append("{0}{1}{2}".format(p[:i],p[i].upper(),p[i+1:]))
        return new
```

# Second solution

```python
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
```
