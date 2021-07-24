import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    v1,v2=map(int,input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

parents=[0 for _ in range(n+1)]
 
def dfs(parent,tree,parents):
    for child in tree[parent]:
        if parents[child]==0: #방문 하지 않음
            parents[child]=parent
            dfs(child,tree,parents)

dfs(1,tree,parents) 
for i in range(2,n+1):
    print(parents[i])
    
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self,parent,data):
        self.parent=parent
        self.Lchild=None
        self.Rchild=None
        self.data=data
    
def find_node(node,t1,t2):
    if node.data==t1:
        newnode=Tree(node,t2)
        if node.Lchild==None:
            node.Lchild=newnode
        else: #node.Rchild==None
            node.Rchild=newnode
    elif node.data==t2:
        newnode=Tree(node,t1)
        if node.Lchild==None:
            node.Lchild=newnode
        else: #node.Rchild==None
            node.Rchild=newnode
    else:
        if node.Lchild!=None:
            find_node(node.Lchild,t1,t2)
        if node.Rchild!=None:
            find_node(node.Rchild,t1,t2)

def find_node_parent(node):
    if node.parent:
        parent[node.data]=node.parent.data
    if node.Lchild!=None:
        find_node_parent(node.Lchild)
    if node.Rchild!=None:
        find_node_parent(node.Rchild)
        
n=int(input())
root=Tree(None,1)

for i in range(n-1):
    a,b=map(int,input().split())
    find_node(root,a,b)

parent=[0]*(n+1)
find_node_parent(root)
for i in range(2,n+1):
    print(parent[i])
'''
