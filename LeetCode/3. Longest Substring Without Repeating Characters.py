class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        max_cnt,cnt=0,0    
        p,q=0,0
    
        while(p<len(s)):
            while(q<len(s)):
                if s[q] not in dic:
                    dic[s[q]]=1
                    cnt+=1
                else:
                    max_cnt=max(max_cnt,cnt)
                    break
                q+=1
            if q==len(s): break
            if s[p] in dic:
                dic.pop(s[p])
                cnt-=1
            p+=1
        print(dic,cnt)
        return max(max_cnt,cnt)

#sliding window & two pointer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len=start=0
        for index,char in enumerate(s):
            if char in used and start <= used[char]:
                start=used[char]+1
            else:
                max_len=max(max_len,(index-start+1))
            used[char]=index
        return max_len
