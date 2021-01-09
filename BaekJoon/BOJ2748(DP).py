import sys

n=int(sys.stdin.readline())
#init fibonacci
fb=[]
fb.append(0)
fb.append(1)
#DP
for i in range(2,n+1):
    fb.append(fb[i-1]+fb[i-2])

print(fb[-1])
