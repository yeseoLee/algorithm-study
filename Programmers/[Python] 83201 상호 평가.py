def solution(scores):
    answer = ''
    len_s=len(scores)
    for i in range(len_s):
        others=[]
        #get average
        for j in range(len_s):
            if i!=j:
                others.append(scores[j][i])
        if min(others) <= scores[i][i] <= max(others):
            others.append(scores[i][i])
        #get grade
        grade="ABCDF"
        avg=sum(others)/len(others)
        if avg >=90:
            answer+='A'
        elif avg >=80:
            answer+='B'
        elif avg >=70:
            answer+='C'
        elif avg >=50:
            answer+='D'
        else:
            answer+='F'
    return answer
