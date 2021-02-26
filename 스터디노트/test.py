## 제너레이터를 이용해서 조합 구현 (중복 조합 X)
def combinations(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            print([array[i]])
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                print([array[i]] + next)
                yield [array[i]] + next

result = list(combinations([1,2,3,4],3))
print(result)
