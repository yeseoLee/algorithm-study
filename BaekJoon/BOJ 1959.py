m,n = map(int,input().split(' ')) 
y,x=1,1
  
if(m>n): #세로>가로
    x+=(n-1)//2
    if(n%2==0): y+=n//2
    else: y+=n//2 +(m-n)

elif(m==n): #가로=세로
    x+=(n-1)//2
    y+=m//2

else: #가로>세로
    if(m%2==0):
        x+=m//2 -1
    else:
        x+=m//2-1 + n-m+1
    y+=m//2

if(m>n):
    print(n*2-1)
else:
    print((m-1)*2)
print(y,x)


