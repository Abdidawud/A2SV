# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0 for _ in range(target+1)]
        dp[0]=1

        for i in range(1,target+1):
            temp=0
            for num in nums:
                if num<=i:
                    temp+=dp[i-num]
                dp[i]=temp
        return dp[target]