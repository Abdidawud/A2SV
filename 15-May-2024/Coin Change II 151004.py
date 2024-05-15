# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        store={}
        def dp(i,sum_):
            if sum_==amount:
                return 1
            if sum_>amount or i>=len(coins):
                return 0

            if (i,sum_) not in store:
                store[(i,sum_)]=dp(i,sum_+coins[i])+dp(i+1,sum_)
            return store[(i,sum_)]
        return dp(0,0)
            
         