class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        max_=float('inf')
        now=0
        while right< len(nums):
            now+=nums[right]
            right+=1
            while now >=target:
                now -=nums[left]
                left+=1
                max_=min(max_,right-left+1)
        if max_==float('inf'):
            return 0
        else:
            return max_