n=int(input())
p=1000000007
'''
a^p-1=1(mod p)
a^p = p (mod p) a * a^p-1

fn+1 = fn + fn-1
fn= fn+0

[fn+1 ]  =  [1 1] [  fn   ]
[   fn  ]      [1 0] [ fn-1 ]

            =  [1 1] ^i [ f1 ]
                [1 0]     [ f0 ]
'''
a=[[1,1],[1,0]]
def matrix_square(a,b):
    if(b==1):
        for i in range(2):
            for j in range(2):
                a[i][j]%=p
        return a
    
    elif(b%2==1):
        now=[[0,0],[0,0]]
        before=matrix_square(a,b-1)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    now[i][j]+=before[i][k]*a[k][j]
                now[i][j]%=p
        return now
    
    else:
        now=[[0,0],[0,0]]
        before=matrix_square(a,b//2)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    now[i][j]+=before[i][k]*before[k][j]
                now[i][j]%=p
        return now

result=matrix_square(a,n)
print(result[1][0])
