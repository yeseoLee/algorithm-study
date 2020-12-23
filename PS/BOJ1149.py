import sys

n=int(sys.stdin.readline()) #집의 수
price=[]*n
s=0
for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    price.append(line)
    
for i in range(1,n):
    price[i][0]+=min(price[i-1][1],price[i-1][2])
    price[i][1]+=min(price[i-1][0],price[i-1][2])
    price[i][2]+=min(price[i-1][0],price[i-1][1])

print(min(price[n-1]))
