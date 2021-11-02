import sys
input = sys.stdin.readline

n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

dp=[500][500]

