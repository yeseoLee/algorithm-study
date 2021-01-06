import sys
n=int(sys.stdin.readline())
distance=list(map(int,sys.stdin.readline().split()))
price=list(map(int,sys.stdin.readline().split()))

lowprice=price[0]
priceSum=0
for i in range(n-1):
    lowprice=min(lowprice,price[i])
    priceSum+=lowprice*distance[i]

print(priceSum)
    
"""
가장 싼 값을 계속 갱신(새 도시의 가격과 비교) 하면서 새 도시 방문
"""
