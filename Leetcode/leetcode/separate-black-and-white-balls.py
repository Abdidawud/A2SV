class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        count=0
        for i in s:
            if i=='1':
                count+=1
            else:
                ans+=count
        return ans