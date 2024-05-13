# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        store={}
        def dp(i,flag):
            if i >= len(prices):
                return 0
            if (i,flag) in store:
                return store[(i,flag)]
            if flag:
                max_=max((prices[i]-fee)+dp(i+1,False),dp(i+1,True))
            else:
                max_=max((-prices[i])+dp(i+1,True),dp(i+1,False))
            store[(i,flag)]=max_
            return max_
        return dp(0,False)
