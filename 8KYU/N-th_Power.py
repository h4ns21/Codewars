# 1

def index(arr, n):
    return arr[n]**n if 0 <= n < len(arr) else -1

# 2

def index(arr, n):
    return arr[n]**n if n < len(arr) else -1
