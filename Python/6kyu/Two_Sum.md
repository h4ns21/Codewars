# First solution

```python
def two_sum(numbers, target):
    for i in range(len(numbers) - 1):  # maintain the first index
        for j in range(i + 1, len(numbers)):  # maintain the second index
            if numbers[i] + numbers[j] == target: # check the sum of both values
                return i, j  # return the indices of each element
```

# Second solution

```python
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
```
