# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        store={}
        def dp(i):
            if i>= len(days):
                return 0
            if i in store:
                return store[i]
            
            oneDay=costs[0]+dp(i+1)
            nextDay=i
            while nextDay<len(days) and days[nextDay]<days[i]+7:
                nextDay+=1
            
            sevenDay=costs[1]+dp(nextDay)

            nextDayII=i
            while nextDayII<len(days) and days[nextDayII]<days[i]+30:
                nextDayII+=1
            
            thirtyDay=costs[2]+dp(nextDayII)
            
            store[i]=min(oneDay,sevenDay,thirtyDay)
            return store[i]
        return dp(0)