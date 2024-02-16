class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        left=0
        right=0
        max_=0
        ans=0

        while right< len(s):
            dic[s[right]]+=1
            max_=max(max_,dic[s[right]])

            if (right-left +1) - max_<=k:
                right+=1
            else:
                while (right-left +1) -max_>k:
                    dic[s[left]]-=1
                    left+=1
                right+=1
            ans=max(ans,right-left)
        return ans