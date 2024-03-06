class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=bisect_left(nums,target)
        y=bisect_right(nums,target)
        ans=[x,y-1]
        if x>len(nums)-1 and y>len(nums)-1:
            ans[:]=[-1,-1]
        elif nums[x]!=target and nums[y]!=target:
            ans[:]=[-1,-1]
        return ans