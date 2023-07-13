import sys
input = sys.stdin.readline

p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))

# gradient
d1 = p2[0] - p1[0], p2[1] - p1[1]
d2 = p3[0] - p2[0], p3[1] - p2[1]

if d1[0]==0: # x축에 대칭   
    sign = 1 if d1[1] > 0 else -1

    if d2[0]==0:
        print(0)
    elif d2[0] > 0:
        print(-1 * sign)
    else:
        print(1 * sign)
    sys.exit(0)
g1 = d1[1] / d1[0]
g2 = (d2[1]) / d2[0]

b = p1[1] - g1 * p1[0]

def f(x):
    return g1*x+b

sign = 1 if d1[0] > 0 else -1


if g1 == g2:
    print(0)
elif f(p3[0]) > p3[1]:
    print(-1 * sign)
else:
    print(1 * sign)
