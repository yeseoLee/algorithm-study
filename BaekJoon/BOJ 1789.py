s=int(input()) #n개의 서로 다른 자연수의 합 s
n=1
x=1
while(x<=s):
    n+=1
    x+=n
print(n-1)
'''
1
1+2
1+2+3
1+2+3+4
1+2+3+4+5
'''
