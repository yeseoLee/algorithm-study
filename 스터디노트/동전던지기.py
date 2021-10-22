import random

test=10
count = 1000
n=1000

print(f"test : {test}")
print(f"count : {count}")
print(f"n : {n}")

for i in range(test):
    diff=[]
    for i in range(count):
        back,forth=0,0
        for j in range(n):
            x = random.randrange(1,3) # 1 or 2
            if x==1: back+=1
            else: forth+=1
        diff.append(abs(back-forth))
    print(sum(diff)/count)
