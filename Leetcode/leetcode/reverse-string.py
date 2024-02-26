def reverse(nums,l,r):
    if l>r:
        return nums
    nums[l],nums[r]=nums[r],nums[l]
    return reverse(nums,l+1,r-1)
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        reverse(s,left,right)