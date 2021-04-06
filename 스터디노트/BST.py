def sibling(x):
    if(x==0): return 0
    elif(x%2==0): return x-1
    else: return x+1

def insert(x):
    i=0
    while(BST[i]!=0):
        if(x>=BST[i]):
            i=i*2+2
        else:
            i=i*2+1
    p=(i-1)//2
    pp=(p-1)//2
    if(i>2 and BST[sibling(p)]==0): #balancing
        if(i%2==p%2):
            BST[sibling(p)]=BST[pp]
            BST[pp]=BST[p]
            BST[p]=x
        else:
            BST[sibling(p)]=BST[pp]
            BST[pp]=x
    else:
        BST[i]=x

def delete():
    i=0
    while(1):
        if(BST[i*2+2]==0):
            k=BST[i]
            BST[i]=0
            if(i==0):
                BST[i]=BST[i*2+1]
                BST[i*2+1]=0
            return k
        i=i*2+2

n=int(input())
BST=[0]*100000
for i in range(n):
    x=int(input())
    if(x==0):
        print(delete())
    else:
        insert(x)
    #print(BST)
