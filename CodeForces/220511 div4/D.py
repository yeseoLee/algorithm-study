import sys
input = sys.stdin.readline

def init_diagonal_sum(n,m,arr):
    if (n==1 or m==1):
        return
    add_sum=[0]*(n+m-1)
    sub_sum=[0]*(n+m-1)
    
    for i in range(n):
        for j in range(m):
            add_sum[i+j]+=arr[i][j]
            sub_sum[i-j+(m-1)]+=arr[i][j]
    return add_sum,sub_sum

def get_max_score_bishop(n,m,arr):
    if (n==1 or m==1):
        return
    add_sum,sub_sum = init_diagonal_sum(n,m,arr)
    max_score=0
    for i in range(n):
        for j in range(m):
            max_score = max(max_score,add_sum[i+j]+sub_sum[i-j+(m-1)] - arr[i][j])
    return max_score

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]

    if (n==1):
        print(max(arr[0]))
    elif (m==1):
        print(max([num for inner_list in arr for num in inner_list]))
    else:
        print(get_max_score_bishop(n,m,arr))
