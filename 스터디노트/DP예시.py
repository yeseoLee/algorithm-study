x=int(input())
dp=[x]
cnt=0

while(True):
    if(1 in dp):
        print(cnt)
        print(dp)
        break
    calc = []
    for i in dp:
        if(i% 2==0):
            calc.append(i/2)
        if(i%3 ==0):
            calc.append(i/3)
        calc.append(i-1)
    dp = calc

    cnt+=1
