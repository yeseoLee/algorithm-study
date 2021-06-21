t=int(input())
for i in range(t):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(2)]
    dp=[[0]*n for _ in range(2)]
    for a in range(2):
        for b in range(n):
