def printStar(n):
    if(n==1):
        return 0
    else:
        for i in range(n):
            if(i%3==1):
                for j in range(n):
                    if(i//(n//3)==1):
                        if(j//(n//3)==1):
                            print(" ",end="")
                        else:
                            if(j%3==1):
                                print(" ",end="")
                            else:
                                print("*",end="")
                    elif(j%3==1):
                        print(" ",end="")
                    else:
                        print("*",end="")
            else:
                for j in range(n):
                    if(i//(n//3)==1):
                        if(j//(n//3)==1):
                            print(" ",end="")
                        else:
                            print("*",end="")
                    else:
                        print("*",end="")
            print("")
            
n=int(input())
printStar(n)
