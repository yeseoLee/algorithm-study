import sys
input = sys.stdin.readline

def get_min_diff(n,m,arr):
    min_diff = (ord('z')-ord('a')) * m
    for i in range(n):
        for j in range(i+1,n):
            min_diff = min(min_diff,get_diff(arr[i],arr[j]))
    return min_diff

def get_diff(str1, str2):
    diff=0
    for x,y in zip(str1,str2):
        diff+=abs(ord(x)-ord(y))
    return diff

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(input().rstrip())
    min_diff = get_min_diff(n,m,arr)
    print(min_diff)
    
