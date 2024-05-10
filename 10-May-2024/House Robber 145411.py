# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        store={}

        def dp(i):
            if i>=len(nums):
                return 0
            if i not in store:
                store[i]=max(nums[i]+dp(i+2),dp(i+1))
            return store[i]
        return dp(0)