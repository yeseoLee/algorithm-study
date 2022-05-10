import sys
input = sys.stdin.readline

def get_count_to_eat(sugar,query):
    counts=[]
    for q in query:
        count=0
        for s in sugar:
            count+=1
            q-=s
            if q<=0:
                counts.append(count)
                break
        else:
            counts.append(-1)
    return counts
                
t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    sugar = list(map(int,input().split()))
    query =[]
    for i in range(q):
        query.append(int(input()))

    counts = get_count_to_eat(sorted(sugar,reverse=True),query)
    for count in counts:
        print(count)
    
    
