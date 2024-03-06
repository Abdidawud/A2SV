class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]
        
        left=0
        right=len(nums)-1
        ans=float('inf')
        while left<=right:
            mid=(right+left)//2
            if nums[mid]<=nums[right]:
                ans=min(ans,nums[mid])
                right=mid-1
            else:
                left=mid+1
        return ans