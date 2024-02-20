class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans=nums[0]
        sum_=nums[0]
        for i in range(1,len(nums)):
            sum_+=nums[i]
            if sum_>nums[i]:
                ans=max(ans,math.ceil(sum_/(i+1)))
        return ans