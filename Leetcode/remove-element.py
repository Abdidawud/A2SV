class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]='_'

        i=0
        j=0
        count=0
        while j<len(nums):
            if nums[j] !='_':
                nums[i],nums[j]= nums[j],nums[i]
                i+=1
            j+=1
        for op in nums:
            if op!="_":
                count+=1
        return count