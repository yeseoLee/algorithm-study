n=int(input())
num=list(map(int,input().split()))
op=list(map(int,input().split()))
mx,mn = - int(1e9), int(1e9)

def solve(index, ans, add, sub, mul, div):
    global mx,mn
    if index == n:
        mx = max(mx,ans)
        mn = min(mn,ans)
        return
    if add > 0:
        solve(index+1, ans+num[index], add-1, sub, mul, div)
    if sub > 0:
        solve(index+1, ans-num[index], add, sub-1, mul, div)
    if mul > 0:
        solve(index+1, ans*num[index], add, sub, mul-1, div)
    if div > 0:
        solve(index+1, int(ans/num[index]), add, sub, mul, div-1)

solve(1, num[0], op[0],op[1],op[2],op[3])
print(mx)
print(mn)