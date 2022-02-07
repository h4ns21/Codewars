# 1

def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'
  
# 2

def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")
