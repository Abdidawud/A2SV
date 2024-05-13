# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        store={}
        def dp(i,sell,cool):
            if i>=len(prices):
                return 0
            if (i,sell,cool) in store:
                return store[(i,sell,cool)]
            
            if sell:
                max_=max(prices[i]+dp(i+2,False,False),dp(i+1,True,True))
            elif not sell and cool:
                max_=dp(i+1,sell,False)
            else:
                max_=max(-prices[i]+dp(i+1,True,False),dp(i+1,False,False))
            store[(i,sell,cool)]=max_
            return max_
        return dp(0,False,False)