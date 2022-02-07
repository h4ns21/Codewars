# 1

def solution(n):
    result = []
    for i in range(1, n):
        if not i % 3 or not i % 5:
            result.append(i)
    return sum(result)

# 2

def solution(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
