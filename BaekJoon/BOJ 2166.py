from sys import stdin


# CCW(counter clockwise) 알고리즘
def CCW(a, b, c):
    # 두 벡터의 외적의 크기는 두 벡터가 만드는 평행사변형의 넓이
    # 반시계 방향: 양수 / 시계 방향: 빠지게 된다.

    ab = (b[0] - a[0], b[1] - a[1])
    ac = (c[0] - a[0], c[1] - a[1])

    return ab[0] * ac[1] - ab[1] * ac[0]


n = int(stdin.readline())
dots = [[0] * 2 for i in range(n)]
for i in dots:
    i[0], i[1] = map(int, stdin.readline().split())


area = 0
for i in range(len(dots) - 1):
    # 다각형이 볼록일 때는 겹치는 영역이 없어(0 또는 양수) 상관없음
    # 오목일 때는 겹치는 삼각형이 생기는데, 이 때 외적 값이 음수이기 때문에 더했을 때 자연스럽게 빠지게 된다.
    area += CCW(dots[0], dots[i], dots[i + 1]) / 2

print(round(abs(area), 1))
