line=input()
apb=[-1]*26
for idx,item in enumerate(line):
    i=ord(item)-ord('a')
    if(apb[i]==-1): apb[i]=idx

for i in apb:
    print(i,end= " ")
