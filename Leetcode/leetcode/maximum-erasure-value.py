class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic={}
        start=0
        max_=0
        current=0
        for i ,num in enumerate(nums):
            if num in dic and dic[num]>=start:
                start=dic[num]+1
                current=sum(nums[start:i+1])
            else:
                current+=num
                max_=max(max_,current)
            dic[num]=i
        return max_