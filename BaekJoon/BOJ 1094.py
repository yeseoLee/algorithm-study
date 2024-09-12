X = int(input())
arr = [64]
while sum(arr) > X:
    arr[-1] //= 2
    if sum(arr) < X:
        arr.append(arr[-1])

print(len(arr))
