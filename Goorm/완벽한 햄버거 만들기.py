n = int(input())
arr = list(map(int, input().split()))

flag = False
result = sum(arr)
for i in range(n - 1):
    if flag and arr[i] < arr[i + 1]:
        result = 0
        break
    if not flag and arr[i] > arr[i + 1]:
        flag = True

print(result)
