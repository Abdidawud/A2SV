# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        store={}
        def dp(n):
            if n==1:
                return 1
            if n not in store:
                max_=0
                for i in range(1,n):
                    max_=max(max_,(n-i)*i,dp(n-i)*i,(n-i)*dp(i))
                store[n]=max_
            return store[n]
        return dp(n)