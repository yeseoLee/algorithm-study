'''메모리 초과
def minC(arr):
    if(len(arr)==1):
        return arr[0]
    elif(len(arr)==2):
        return sum(arr)*2
    else:
        s=1000000000
        for i in range(1,len(arr)):
            s=min(s,minC(arr[:i])+minC(arr[i:]))
        return s
n=int(input())
card=[]
for i in range(n):
    card.append(int(input()))
card=sorted(card)
print(minC(card))
'''
import sys
n=int(input())
card=[]
for i in range(n):
    card.append(int(input()))

if(n==1):
    print(card[0])
    sys.exit()
    
card=sorted(card)
front=[0]*n
front[0]=0
front[1]=card[0]+card[1]
s=front[1]
for i in range(2,n):
    s+=card[i]
    front[i]=front[i-1]+s

card.reverse()
back=[0]*n
back[0]=0
back[1]=card[0]+card[1]
s=back[1]
for i in range(2,n):
    s+=card[i]
    back[i]+=back[i-1]+s

min_cnt=float('inf')
s=sum(card)
front=[0]+front
back=[0]+back
for i in range(n+1):
    min_cnt=min(min_cnt,front[i]+back[n-i]+s)

print(min_cnt)

