# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        sum_=sum(rolls)
        f=(mean*(n+m))-sum_
        if f>n*6 or f<n:
            return []
        ans=[1]*n
        f=f-n
        i=0
        while f>0 and i<=len(ans):
            if i==len(ans):
                i=0
            ans[i]+=1
            f-=1
            i+=1
        return ans