import sys

n= int(sys.stdin.readline())
cnt=[99999 for i in range(n*3)]

cnt[1]=0

for i in range(1,n):
    cnt[i+1]=min(cnt[i]+1,cnt[i+1])
    cnt[i*2]=min(cnt[i]+1,cnt[i*2])
    cnt[i*3]=min(cnt[i]+1,cnt[i*3])

print(cnt[n])
