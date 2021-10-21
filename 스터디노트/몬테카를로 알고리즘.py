import random
n = 100000 #반복 횟수
r = 3 #제곱근 값을 구할 숫자
k=0

for i in range(n):
    x = random.uniform(0,r)
    if x**2 < r: k+=1

print(k*r/n)
