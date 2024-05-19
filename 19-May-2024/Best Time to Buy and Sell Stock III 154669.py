# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        store={}
        def dp(i,buy,trans):
            if i>=len(prices):
                return 0
            if trans >2:
                return 0
            
            if (i,buy,trans) in store:
                return store[(i,buy,trans)]
            
            if buy:
                ans=max(-prices[i]+dp(i+1,0,trans),dp(i+1,1,trans))
            else:
                ans=max(prices[i]+dp(i+1,1,trans+1),dp(i+1,0,trans))
            store[(i,buy,trans)]=ans
            return store[(i,buy,trans)]
        return dp(0,1,1)