import math
Min,Max=map(int,input().split())
square=[True for _ in range(Min,Max+1)]
for i in range(2,int(math.sqrt(Max)+1)):
    step=(i**2)
    start=step*((Min-1)//step +1)
    for j in range(start,Max+1,step):
        square[j-Min]=False

#print(square)
print(sum(square))
