class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum=[]
        sum_=0
        for i in nums:
            sum_+=i
            prefix_sum.append(sum_)
        lenn=len(nums)-1
        ans=[]
        for i in range(len(prefix_sum)):
            val=abs((sum_-prefix_sum[i])-(nums[i]*(lenn-i)))+abs((nums[i]*(i+1))-prefix_sum[i])
            ans.append(val)
        return ans