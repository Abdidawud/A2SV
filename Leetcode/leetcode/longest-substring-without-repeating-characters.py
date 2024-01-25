class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        c=Counter()
        ans=0
        while right<len(s):
            if c[s[right]]==1:
                c[s[left]]-=1
                left+=1
            else:
                c[s[right]]+=1

                ans=max(ans,right-left+1)
                right+=1
        
        return ans