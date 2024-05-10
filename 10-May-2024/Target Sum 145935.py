# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        store={}
        def dp(i,sum_):
            if i==len(nums):
                if target==sum_:
                    return 1
                else:
                    return 0
            
            if (i,sum_) not in store:
                store[(i,sum_)]=dp(i+1,sum_+nums[i])+dp(i+1,sum_ -nums[i])
            return store[(i,sum_)]
        return dp(0,0)