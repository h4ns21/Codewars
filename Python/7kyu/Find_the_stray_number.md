# First solution 

```python
def stray(arr):
    list = []
    for i in arr:
        if arr.count(i) < 2:
            list.append(i)
    for i in list:
        return i
    # return [i for i in arr if arr.count(i) < 2] --> [number]
```

# Second solution

```python
def stray(arr):
    return min(arr, key=arr.count)
```
