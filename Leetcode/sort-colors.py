class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        m = 0
        R = len(nums)-1
        while m<len(nums):
            if m>R:
                break
            if nums[m]==0:
                nums[L], nums[m] = nums[m], nums[L]
                print(nums)
                L+=1

            elif nums[m]==2:
                nums[m], nums[R] = nums[R], nums[m]
                print(nums)
                R-=1
                m-=1
            m+=1