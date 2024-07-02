n, k = map(int, input().split())
arr = list(map(int, input().split()))


def count_ones_in_binary(num):
    cnt = 0
    while num > 0:
        num, r = divmod(num, 2)
        if r:
            cnt += 1
    return cnt


new_arr = [(x, count_ones_in_binary(x)) for x in arr]
new_arr.sort(key=lambda x: (-x[1], -x[0]))
print(new_arr[k - 1][0])
