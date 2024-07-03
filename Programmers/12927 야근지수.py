import heapq


def solution(n, works):
    # works의 제곱합을 최소화
    if n >= sum(works):
        return 0

    heap = []
    for work in works:
        heapq.heappush(heap, -work)

    for i in range(n):
        work = heapq.heappop(heap)
        heapq.heappush(heap, work + 1)

    answer = sum(x**2 for x in heap)
    return answer
