import sys
input=sys.stdin.readline

def get_sub(n,l):
    if l>100:
        return -1
    if l%2==0:
        if (n//l * 2 +1)*(l//2) == n and n//l - l//2+1>=0:
            return ' '.join(str(x) for x in range(n//l - l//2+1, n//l + l//2 + 1))
        else:
            return get_sub(n,l+1)
    else:
        if n%l==0 and n//l - l//2>=0:
            return ' '.join(str(x) for x in range(n//l - l//2, n//l + l//2 +1))
        else:
            return get_sub(n,l+1)

n,l=map(int,input().split())
print(get_sub(n,l))
