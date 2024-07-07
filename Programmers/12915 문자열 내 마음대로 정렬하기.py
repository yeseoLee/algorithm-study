def solution(strings, n):
    arr = sorted(strings, key=lambda x: (x[n], x))
    return arr
