# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        # n = len(piles)
        # memo = {}
        # def dp(i,j):

        #     if i == j:
        #         return piles[i]
        #     if (i,j) not in memo:
        #         left = dp(i+1,j) + piles[i]
        #         right = dp(i,j-1) + piles[j]
        #         memo[(i,j)]= max(left,right)
        #     return memo[(i,j)]
        # ans = dp(0,n-1)
        # return sum(piles) - ans < ans