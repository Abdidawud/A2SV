class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        dic=defaultdict(int)
        ans=0
        for i in s:
            if i=='(':
                dic[i]+=1
                ans+=1
            else:
                if dic['(']>=1:
                    ans-=1
                    dic['(']-=1
                else:
                    ans+=1
        return ans