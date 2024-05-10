# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target %2 !=0:
            return False
        store={}
        def dp(i,target):
            if target==0:
                return True
            if i>=len(nums) or target<0:
                return False
            state=(i,target)
            if state not in store:
                store[state]=dp(i+1,target-nums[i]) or dp(i+1,target)
            return store[state]
        return dp(0,target//2)
            