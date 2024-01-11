class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i=0
        j=0
        ans=[]
        op=0
        while i < len(nums):
            
            for j in nums:
                if nums[i]>j:
                    op+=1
            ans.append(op)
            i+=1
            op=0

        return ans