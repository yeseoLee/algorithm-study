def solution(s):
    answer=len(s)
    for i in range(1,len(s)//2+1):
        ans=''
        f=0
        for j in range(0,len(s),i):
            if(s[j:j+i]==s[j+i:j+i+i]):
                f+=1
            else:
                f=0
                ans+=str(f)+s[j:j+i]
        if(f!=0):
            ans+=str(f)+s[j:j+i]
        print(ans)
        answer=min(answer,len(ans))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
