# First method

```python
def reverse_words(text):
    words = text.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence
```

# Second method

```python
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(" "))
```
