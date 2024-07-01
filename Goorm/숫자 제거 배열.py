n, k = map(int, input().split())
arr = list(map(int, input().split()))


def is_a_contain_b(a: int, b: int) -> bool:
    a = str(a)
    b = str(b)
    for i in range(len(a) - len(b) + 1):
        if a[i : i + len(b)] == b:
            return True
    return False


new_arr = [x for x in arr if not is_a_contain_b(x, k)]
print(len(new_arr))
