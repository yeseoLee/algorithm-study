#순열과 조합 라이브러리 : itertools
import itertools
print(list(itertools.permutations([1,2,3])))
print(list(itertools.combinations([1,2,3],2)))

#순열 구현
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
print(sorted(permute([1,2,3])))

#조합 구현
