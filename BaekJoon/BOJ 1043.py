n,m=map(int,input().split())
true=list(map(int,input().split()))
true=true[1:]
party=[]
for _ in range(m):
    x=list(map(int,input().split()))
    if(len(x)!=1):
        party.append(x[1:])

i=0
while(1):
    if(len(true)<=i):
        break
    for j in party:
        if true[i] in j:
            true+=j
            party.remove(j)
    i+=1

print(len(party))    
            
        
    
