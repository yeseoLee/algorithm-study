import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
op=list(map(int,input().split()))
mx,mn = -1e9,1e9

def solve(index, ans, add, sub, mul, div):
    global mx,mn
    if index == n:
        mx = max(mx,ans)
        mn = min(mn,ans)
        return
    if add:
        solve(index+1, ans+num[index], add-1, sub, mul, div)
    if sub:
        solve(index+1, ans-num[index], add, sub-1, mul, div)
    if mul:
        solve(index+1, ans*num[index], add, sub, mul-1, div)
    if div:
        solve(index+1, ans//num[index] if ans > 0
              else -((-ans)//num[index]), add, sub, mul, div-1)

solve(1, num[0], op[0],op[1],op[2],op[3])
print(f"{mx}\n{mn}")
