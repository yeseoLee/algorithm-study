n=int(input())
cnt=0
new=n
while(True):
    if(new<10):
        new=new*10+new
    elif(new>=10):
        new=(new%10)*10+((new//10)+(new%10))%10
    cnt+=1
    if(new==n): break
print(cnt)
