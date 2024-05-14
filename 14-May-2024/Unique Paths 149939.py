# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store=[[0]*(n+1) for _ in range(m+1)]
        def dp(m,n):
            if store[m][n] !=0:
                return store[m][n]
            if m==1:
                return 1
            if n==1:
                return 1
            store[m][n]=dp(m-1,n) + dp(m,n-1)
            return store[m][n]
        return dp(m,n)