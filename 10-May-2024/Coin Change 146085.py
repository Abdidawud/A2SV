# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        store={}
        def dp(target):
            if target==0:
                return 0
            if target<0:
                return float("inf")
            if target in store:
                return store[target]
            
            ans=float("inf")

            for i in coins:
                if i<=target:
                    ans=min(ans,1+dp(target-i))
            store[target]=ans
            return ans
        
        ans=dp(amount)
        return ans if ans != float("inf") else -1