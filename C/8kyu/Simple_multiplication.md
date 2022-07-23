# First solution

```c
int simple_multiplication(int number) {
    if (number % 2 == 0)
        return number*8;
    else
        return number*9;
}
```

# Second solution

```c
int simple_multiplication(int number) {
    return number % 2 == 0 ? number*8 : number*9;
}
```
