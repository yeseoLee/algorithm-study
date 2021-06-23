n=int(input())
rope=[]
for i in range(n):
    rope.append(int(input()))

rope=sorted(rope,reverse=True)
weight=0
for i,v in enumerate(rope):
    weight=max((i+1)*v,weight)
print(weight)
