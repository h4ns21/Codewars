# First method

```python
def move_ten(st): 
    cipherText = ""
    for ch in st:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + 10 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter

    return cipherText
```

# Second method

```python
def move_ten(st):
  return ''.join(chr(ord(char)+10) if i<'q' else chr(ord(i)-16) for char in st)
```
