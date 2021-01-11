mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
mylen=len(mylist)
answer=[[0 for i in range(mylen)]for j in range(mylen)]
for i in range(mylen):
    for j in range(mylen):
        answer[j][i]=mylist[i][j]

print(mylist)
print(answer)
