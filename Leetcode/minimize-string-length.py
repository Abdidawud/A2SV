class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        ans=[]

        for i in s:
            if i in ans:
                continue
            else:
                ans.append(i)
        return (len(ans))
