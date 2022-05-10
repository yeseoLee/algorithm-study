import sys
input = sys.stdin.readline

def get_count_ate_candy(arr):
    return sum(arr) - min(arr)*len(arr)

t=int(input())
for i in range(t):
    n= int(input())
    arr=list(map(int,input().split()))
    print(get_count_ate_candy(arr))
    
    
