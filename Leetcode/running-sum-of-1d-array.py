class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        running_sum=0
        for i in nums:
            running_sum+=i
            ans.append(running_sum)
        return ans