class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        general_set=set(nums)
        i=0
        j=0
        ans=0
        while i<len(nums):
            small_set=set()
            while j<len(nums):
                small_set.add(nums[j])
                if small_set==general_set:
                    ans+=1
                j+=1
            i+=1
            j=i
        return ans