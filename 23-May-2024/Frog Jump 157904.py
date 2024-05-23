# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n=len(stones)
        dp=[[False]*(n+1) for _ in range(n)]
        dp[0][0]=True

        stone_index={stone:i for i,stone in enumerate(stones)}

        for i in range(n):
            for k in range(n):
                if dp[i][k]:
                    for step in [k-1,k,k+1]:
                        if step>0 and stones[i]+step in stone_index:
                            dp[stone_index[stones[i]+step]][step]=True
        
        return any(dp[n-1])