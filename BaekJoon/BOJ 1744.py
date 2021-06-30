import sys
input=sys.stdin.readline
n=int(input())
pos=[]
neg=[]
s=0

for i in range(n):
    x=int(input())
    if(x<=0): neg.append(x)
    elif(x==1): s+=1
    else: pos.append(x)
    
pos.sort(reverse=True)
neg.sort()

for i in range(0,len(neg)-1,2):
    s+=neg[i]*neg[i+1]
if(len(neg)%2):
    s+=neg[-1]
for i in range(0,len(pos)-1,2):
    s+=pos[i]*pos[i+1]
if(len(pos)%2):
    s+=pos[-1]

print(s)

