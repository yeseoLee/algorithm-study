def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort()

    for a, b in zip(A, B):
        answer += a * b

    return answer
