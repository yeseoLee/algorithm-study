# BOJ 19532

import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())

def discrimination(x,y):
    return a*x+b*y==c and d*x+e*y == f 
def get_y(x):
    if b!=0:
        return (c-a*x) // b
    elif e!=0:
        return (f-d*x) // e
    else :
        return None # exception

# brute force
def brute_force(start, end):
    for x in range(start,end+1):
        y = get_y(x) 
        if discrimination(x,y):
            return x,y
    return None

# math
def math():
    if a*e-d*b==0: # 해가 없거나 무수히 많음
        return None
    x = (c*e-f*b) // (a*e-d*b)
    y = get_y(x)
    return x,y

print(*brute_force(-999,999))
# print(*math())
