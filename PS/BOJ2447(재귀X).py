def printStar(n):
    star = [["*"]*n for i in range(n)]
    v=n; cnt=0
    while(v!=1):
        v//=3
        cnt+=1

    for cnt_ in range(cnt):
        idx= [i for i in range(n) if ((i // 3 ** cnt_) % 3==1)] #빈칸 idx
        for i in idx:
            for j in idx:
                star[i][j]=" "
    #출력
    for i in range(n):
        for j in range(n):
           print(star[i][j],end="")
        print("")
    
    #print('\n'.join([''.join([str(i) for i in row]) for row in star]))
        
n=int(input())
printStar(n)
