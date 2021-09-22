'''
x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1
y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1

1:1 (1) / 2:2 (2)
네 개의 정수 M, N, x와 y가 주어질 때,
<M:N>이 카잉 달력의 마지막 해라고 하면
<x:y>는 몇 번째 해를 나타내는지 구하는 프로그램을 작성하라. 
'''

'''
    10 12 3 9

    x -> x + m * (k)  3, 13, 23, 33....
    y -> y + n * (k) 9, 21, 33, ....

    (m-n) * k + (x-y) = 0
'''
import sys
input = sys.stdin.readline

t=int(input())
for i in range(t):
    m,n,x,y = map(int,input().split())
    tmp=x
    while(tmp <= m*n):
        if (tmp-y) % n ==0:
            print(tmp)
            break
        tmp+=m
    else:
        print(-1)

#재귀함수
def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))



    
