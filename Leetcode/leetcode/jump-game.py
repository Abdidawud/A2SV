class Solution:
    def canJump(self, nums: List[int]) -> bool:
        key=len(nums) -1
        ans=0
        for i in range(len(nums)):
            ans=max(ans-1,nums[i])
            if ans <= 0 and i < len(nums)-1:
                return False  

        return True