# First method

```python
def basic_op(operator, v1, v2):
    if operator == '+':
        return v1+v2
    elif operator == '-':
        return v1-v2
    elif operator == '*':
        return v1*v2
    else:
        return v1/v2
```
# Second method

```python
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))
```

# Third method

```python
def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)
```
