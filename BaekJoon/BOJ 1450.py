''' TimeLimit
import sys
input=sys.stdin.readline
n,c=map(int,input().split()) #n: 물건 개수, c: 최대 용량
items=list(map(int,input().split()))
items=sorted(items)

cnt=1
def func(start,now):
    global cnt
    for i in range(start,n):
        now+= items[i]
        if now>c:
            break
        else:
            cnt+=1
            func(i+1,now)
        now-=items[i]

func(0,0)
print(cnt)
'''

''' binarysearch
import sys

N, C = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split())) 
left = weight[:N // 2] 
right = weight[N // 2:] 
lsum = [] 
rsum = [] 

def bruteforce(st, end, warr, sumarr): 
    if st >= len(warr): 
        sumarr.append(end) 
        return     
    bruteforce(st + 1, end, warr, sumarr) #선택안하고 
    bruteforce(st + 1, end + warr[st], warr, sumarr)  #선택하고
 
def binarysearch(start, end, arr, target): 
    while start < end: 
        mid = (start + end) // 2 
        if arr[mid] <= target: 
            start = mid + 1 
        else: 
            end = mid 
    return end #정렬 되어있기 때문에 target보다 작은 값의 개수를 반환

bruteforce(0, 0, left, lsum) 
bruteforce(0, 0, right, rsum) 
rsum.sort() 

result = 0 
for i in lsum: 
    if C - i >= 0: 
        result += binarysearch(0, len(rsum), rsum, C - i) 
    
print(result)
'''

#Two Pointer
import sys

N, C = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split())) 
left = weight[:N // 2] 
right = weight[N // 2:] 
lsum = [] 
rsum = []
result=0

#now_idx, now_sum, weight, lsum or rsum
def dfs(idx,now,warr,sumarr):
    if idx >= len(warr):
        sumarr.append(now)
        return
    dfs(idx+1,now,warr,sumarr) #미포함
    dfs(idx+1,now+warr[idx],warr,sumarr) #포함

dfs(0,0,left,lsum)
dfs(0,0,right,rsum)
lsum.sort()
rsum.sort()

rp=len(rsum)-1
for lp in range(len(lsum)):
    while rp>=0 and lsum[lp]+rsum[rp] > C:
        rp-=1
    if rp<0:
        break
    result+=rp+1

print(result)
