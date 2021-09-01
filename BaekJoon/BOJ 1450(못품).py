import sys
input=sys.stdin.readline
n,c=map(int,input().split()) #n: 물건 개수, c: 최대 용량
items=list(map(int,input().split()))

items=[item for item in sorted(items) if item<=c]

cnt=1+n #아무것도 안넣었을 때+하나만 넣었을 때



'''
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
