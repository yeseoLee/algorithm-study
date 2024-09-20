def solution(N, arr):
    min_liquid = float("inf")
    recipe = []
    for i in range(N - 2):
        s, e = i + 1, N - 1
        while s < e:
            liquid = arr[i] + arr[s] + arr[e]
            if abs(liquid) < min_liquid:
                min_liquid = abs(liquid)
                recipe = [arr[i], arr[s], arr[e]]
            if liquid == 0:
                break
            elif liquid < 0:
                s += 1
            else:
                e -= 1
    return recipe


N = int(input())
arr = sorted(list(map(int, input().split())))
recipe = solution(N, arr)
print(*recipe)
