class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(substring):
            char_set=set()
            for char in substring:
                char_set.add(char)
            for i in substring:
                if i.isupper():
                    lower=i.lower()
                    if lower not in char_set:
                        return False
                elif i.islower():
                    upper=i.upper()
                    if upper not in char_set:
                        return False
            return True
        
        ans=""
        n=len(s)
        for i in range(n):
            for j in range(1,n):
                substring=s[i:j+1]
                if helper(substring) and len(substring) > len(ans):
                    ans=substring
        return ans
                