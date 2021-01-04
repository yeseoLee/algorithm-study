import sys
s1=input()
s2=input()
s1='0'+s1
s2='0'+s2
lcs=[[0 for i in range(len(s2))] for j in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if(i==0 or j==0):
            lcs[i][j]=0
            continue
        if(s1[i]==s2[j]):
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])

print(lcs[len(s1)-1][len(s2)-1])

"""LCS 알고리즘"""
