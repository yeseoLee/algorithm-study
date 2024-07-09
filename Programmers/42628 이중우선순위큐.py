import heapq


def solution(operations):
    answer = []
    heap = []

    for op in operations:
        op = op.split()

        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        elif op[0] == "D" and len(heap) != 0:
            if op[1] == "1":
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)

    if len(heap) == 0:
        return [0, 0]

    return [max(heap), min(heap)]
